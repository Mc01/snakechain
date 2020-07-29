from __future__ import annotations

from typing import TYPE_CHECKING, Generator, Optional

from couchbase.bucket import Bucket
from couchbase.cluster import Cluster, ClusterOptions, PasswordAuthenticator
from couchbase.collection import CBCollection
from couchbase.exceptions import BucketNotFoundException, ProtocolException
from couchbase.management.admin import Admin

from ..config import (
    STORAGE_HOST,
    STORAGE_USER,
    STORAGE_PASSWORD,
    STORAGE_BUCKET,
    STORAGE_LATEST_KEY,
    GENESIS_HASH,
    STORAGE_CONFIG_COLLECTION,
    STORAGE_BLOCK_COLLECTION,
)
from ..exceptions import InitError

if TYPE_CHECKING:
    from ..block import Block


# noinspection SqlNoDataSourceInspection
class Storage:
    def __init__(self):
        self.cluster: Cluster = Cluster(
            connection_string=f'couchbase://{STORAGE_HOST}',
            options=ClusterOptions(
                authenticator=PasswordAuthenticator(
                    username=STORAGE_USER,
                    password=STORAGE_PASSWORD,
                ),
            )
        )
        try:
            self.bucket = self.cluster.bucket(
                name=STORAGE_BUCKET,
            )
        except BucketNotFoundException:
            storage_management = Admin(
                username=STORAGE_USER,
                password=STORAGE_PASSWORD,
                host=STORAGE_HOST,
            )
            storage_management.bucket_create(
                name=STORAGE_BUCKET,
                ram_quota=256,
            )
            initialized = self._init_bucket(storage_management)
            if not initialized:
                raise InitError

        self.blocks: CBCollection = self.bucket.collection(STORAGE_BLOCK_COLLECTION)
        self.config: CBCollection = self.bucket.collection(STORAGE_CONFIG_COLLECTION)

    def _init_bucket(self, storage_management, max_retries=3) -> bool:
        for i in range(stop=max_retries):
            try:
                storage_management.wait_ready(
                    name=STORAGE_BUCKET,
                )
                self.bucket: Bucket = self.cluster.bucket(
                    name=STORAGE_BUCKET,
                )
                index_management = self.cluster.query_indexes()
                index_management.create_primary_index(STORAGE_BUCKET)
                return True
            except ProtocolException:
                continue
        return False

    def save_block_to_storage(self, block: Block):
        """
        Saves to storage during new block creation
        """
        self.blocks.insert(
            key=block.hash,
            value=block.__dict__,
        )
        self.config.upsert(
            key=STORAGE_LATEST_KEY,
            value=block.hash,
        )

    def get_last_block_from_storage(self) -> Optional[Block]:
        """
        Reads latest block from storage during blockchain init
        """
        latest_hash_exist: bool = self.config.exists(
            key=STORAGE_LATEST_KEY,
        ).exists
        if latest_hash_exist:
            latest_hash: str = self.config.get(
                key=STORAGE_LATEST_KEY,
            ).content
            return self.get_block_from_storage(
                block_hash=latest_hash,
            )
        else:
            return None

    def get_block_from_storage(self, block_hash: str) -> Optional[Block]:
        from ..block import Block
        if self.blocks.exists(
                key=block_hash,
        ).exists:
            block = self.blocks.get(
                key=block_hash,
            ).content
            return Block(**block)
        else:
            return None

    def yield_blocks_from_storage(self) -> Generator[Block]:
        """
        Reads blocks from storage memory efficiently
        Performed during blockchain integrity check
        """
        from ..block import Block
        validated_chain = 0
        previous_hash = GENESIS_HASH
        while previous_hash:
            result = self.bucket.query(
                f'SELECT * FROM {STORAGE_BUCKET} WHERE {STORAGE_BUCKET}.previous_hash = "{previous_hash}"',
            )
            assert result.meta['status'] == 'success'
            count = result.meta['metrics']['resultCount']
            if not count:
                break
            elif count > 1:
                raise Exception(
                    f'Integrity error - hash {previous_hash} returns multiple rows',
                )
            else:
                block_data = next(iter(result))[STORAGE_BUCKET]
                block = Block(**block_data)
                previous_hash = block.hash
                validated_chain += 1
                yield block

    def get_block_count(self) -> int:
        block_count = 'BLOCK_COUNT'
        result = self.bucket.query(
            f'SELECT COUNT(*) AS {block_count} '
            f'FROM {STORAGE_BUCKET} '
            f'WHERE {STORAGE_BUCKET}.previous_hash IS NOT NULL'
        )
        assert result.meta['status'] == 'success'
        response: dict = next(iter(result))
        return response.get(block_count)

    def get_data_size(self) -> int:
        """
        Returns number of bytes used by blocks
        """
        data_size = 'DATA_SIZE'
        result = self.bucket.query(
            f'SELECT SUM(ENCODED_SIZE(default)) AS {data_size} FROM default'
        )
        assert result.meta['status'] == 'success'
        response: dict = next(iter(result))
        return response.get(data_size)
