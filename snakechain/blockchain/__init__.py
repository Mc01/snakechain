from typing import List, Optional

from .block import Block, GenesisBlock
from .buffer import Buffer
from .config import (
    SPACER,
    NUMBER_OF_BLOCKS_IN_MEMORY,
    GENESIS_HASH,
)
from .integrity import IntegrityCheck
from .storage import Storage


class Blockchain:
    def __init__(self):
        # Create Buffer and Storage
        self.buffer: Buffer = Buffer()
        self.storage: Storage = Storage()

        # Run integrity check
        self._integrity_check()

        # Load last block from Storage
        # Or fallback to Genesis Block (which is virtual block)
        last_block: Block = self.storage.get_last_block_from_storage()
        if last_block:
            self.blocks: List[Block] = [last_block]
            self.previous_block_hash = last_block.hash
            self.next_block_number = last_block.header.number + 1
        else:
            self.blocks: List[Block] = []
            self.previous_block_hash = GENESIS_HASH
            self.next_block_number = 1

    def _integrity_check(self):
        print("Starting integrity check", flush=True)
        print(SPACER, flush=True)

        # Create Integrity Check object
        integrity_check: IntegrityCheck = IntegrityCheck()

        # Iterate blocks from Storage memory efficiently
        # And validate each block by Integrity Check
        for existing_block in self.storage.yield_blocks_from_storage():
            integrity_check.validate_block(latest_block=existing_block,)

        # Validate that all blocks are fitting Integrity Check validation
        validated_blocks = integrity_check.validated_count
        total_blocks = self.storage.get_block_count()
        print(
            f"Validated blocks by integrity check: " f"{validated_blocks}", flush=True,
        )
        print(
            f"Total blocks in storage: " f"{total_blocks}", flush=True,
        )
        print(SPACER, flush=True)
        assert validated_blocks == total_blocks

    def append_element(self, element: str):
        """
        Add element for next block body to Buffer
        """
        self.buffer.add_body_element(
            block_number=self.next_block_number, body_element=element,
        )

    def _restrict_memory(self):
        """
        Keeps blocks in Buffer below or equal NUMBER_OF_BLOCKS_IN_MEMORY
        """
        if len(self.blocks) > NUMBER_OF_BLOCKS_IN_MEMORY:
            oldest_block_number: int = self.blocks[0].header.number
            self.buffer.remove_body(oldest_block_number)
            self.blocks.pop(0)

    def create_block(self) -> Block:
        # Create block object
        new_block = Block(
            number=self.next_block_number,
            previous_hash=self.previous_block_hash,
            data=self.buffer.get_body(self.next_block_number),
        )
        self.blocks.append(new_block)

        # Save block to Storage
        self.storage.save_block_to_storage(block=new_block)

        # Increment counters
        self.previous_block_hash = new_block.hash
        self.next_block_number += 1

        # Restrict Buffer after creation
        self._restrict_memory()

        return new_block

    def get_block(self, block_hash: str) -> Optional[Block]:
        # Handle genesis block
        if block_hash == GENESIS_HASH:
            return GenesisBlock()

        # Search within last blocks in Buffer
        hash_to_block_map = {b.hash: b for b in self.blocks}
        if block_hash in hash_to_block_map.keys():
            return hash_to_block_map[block_hash]

        # Fallback to search in Storage
        return self.storage.get_block_from_storage(block_hash=block_hash)

    def get_statistics(self) -> dict:
        return {
            "number of blocks": self.next_block_number - 1,
            "total size in bytes": self.storage.get_data_size() or 0,
        }

    # noinspection PyMethodMayBeStatic
    def start_node(self):
        print("Starting blockchain node", flush=True)
        print(SPACER, flush=True)
        print("Listening for new blocks", flush=True)
        while True:
            continue
