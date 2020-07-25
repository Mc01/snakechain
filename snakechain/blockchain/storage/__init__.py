from __future__ import annotations

from typing import TYPE_CHECKING, Generator, Optional

from couchbase.cluster import Cluster, ClusterOptions, PasswordAuthenticator

from ..config import (
    STORAGE_HOST,
    STORAGE_USER,
    STORAGE_PASSWORD,
)

if TYPE_CHECKING:
    from ..block import Block


class Storage:
    def __init__(self):
        self.cluster = Cluster(
            connection_string=f'couchbase://{STORAGE_HOST}',
            options=ClusterOptions(
                authenticator=PasswordAuthenticator(
                    STORAGE_USER,
                    STORAGE_PASSWORD,
                ),
            )
        )

    @staticmethod
    def save_block_to_storage(block: Block):
        """
        Saves to file during new block creation
        """
        # mode = 'a+'
        # with open(BLOCKCHAIN_STORAGE_FILE, mode) as f:
        #     f.write(f'{block.to_json()}{os.linesep}')
        pass

    @staticmethod
    def get_last_block_from_storage() -> Optional[Block]:
        """
        Reads latest block from file during blockchain init
        """
        # from ..block import Block
        # try:
        #     with open(BLOCKCHAIN_STORAGE_FILE, 'rb+') as f:
        #         f.seek(-2, os.SEEK_END)
        #         while f.read(1) != b'\n':
        #             f.seek(-2, os.SEEK_CUR)
        #         last_line = f.readline().decode()
        #     return Block.from_json(data=last_line)
        # except IOError:
        #     return None
        pass

    @staticmethod
    def yield_blocks_from_storage() -> Generator[Block]:
        """
        Reads blocks from file memory efficiently
        Performed during blockchain integrity check
        """
        # from ..block import Block
        # with open(BLOCKCHAIN_STORAGE_FILE, 'r+') as f:
        #     for line in f:
        #         yield Block.from_json(data=line)
        pass
