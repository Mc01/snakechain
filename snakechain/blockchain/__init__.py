from typing import List

from .block import Block
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
        self.buffer: Buffer = Buffer()
        self.storage: Storage = Storage()
        self._integrity_check()

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
        print('Starting integrity check', flush=True)
        print(SPACER, flush=True)
        integrity_check: IntegrityCheck = IntegrityCheck()

        for existing_block in self.storage.yield_blocks_from_storage():
            integrity_check.validate_block(
                latest_block=existing_block,
            )

        validated_blocks = integrity_check.validated_count
        total_blocks = self.storage.get_block_count()
        print(
            f'Validated blocks by integrity check: '
            f'{validated_blocks}',
            flush=True,
        )
        print(
            f'Total blocks in storage: '
            f'{total_blocks}',
            flush=True,
        )
        print(SPACER, flush=True)
        assert validated_blocks == total_blocks

    def append_element(self, element: str):
        self.buffer.add_body_element(
            block_number=self.next_block_number,
            body_element=element,
        )

    def _restrict_memory(self):
        if len(self.blocks) > NUMBER_OF_BLOCKS_IN_MEMORY:
            oldest_block_number: int = self.blocks[0].header.number
            self.buffer.remove_body(oldest_block_number)
            self.blocks.pop(0)

    def create_block(self) -> Block:
        new_block = Block(
            number=self.next_block_number,
            previous_hash=self.previous_block_hash,
            data=self.buffer.get_body(self.next_block_number),
        )
        self.blocks.append(new_block)
        self.storage.save_block_to_storage(block=new_block)

        self.previous_block_hash = new_block.hash
        self.next_block_number += 1

        self._restrict_memory()

        return new_block

    def start_node(self):
        print('Starting blockchain node', flush=True)
        print(SPACER, flush=True)

        # 1st block
        self.append_element(element='one')
        first_block = self.create_block()
        first_json = first_block.__dict__

        print(
            f'First block: {first_block}',
            flush=True,
        )
        print(
            f'First JSON: {first_json}',
            flush=True,
        )
        print(SPACER, flush=True)

        # 2nd block
        self.append_element(element='two')
        self.append_element(element='three')
        self.append_element(element='four')
        second_block = self.create_block()
        second_json = second_block.__dict__

        print(
            f'Second block: {second_block}',
            flush=True,
        )
        print(
            f'Second JSON: {second_json}',
            flush=True,
        )
        print(SPACER, flush=True)

        print('Listening for new blocks', flush=True)
        while True:
            continue
