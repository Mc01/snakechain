from blockchain.block import Block
from blockchain.config import SPACER
from blockchain.utils import write_block


class Blockchain:
    def __init__(self):
        self.blocks = []
        self.previous_block_hash = '0x0'
        self.next_block_number = 1

    @staticmethod
    def _append_element(element: str):
        Block.append(element)

    def _create_block(self) -> Block:
        new_block = Block(
            number=self.next_block_number,
            previous_hash=self.previous_block_hash,
        )
        self.blocks.append(new_block)

        self.previous_block_hash = new_block.hash
        self.next_block_number += 1
        return new_block

    def start_node(self):
        print('Starting blockchain node', flush=True)
        print(SPACER, flush=True)

        # 1st block
        self._append_element(element='one')
        first_block = self._create_block()
        first_json = first_block.to_json()
        write_block(first_block, truncate=True)

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
        self._append_element(element='two')
        self._append_element(element='three')
        self._append_element(element='four')
        second_block = self._create_block()
        second_json = second_block.to_json()
        write_block(second_block)

        print(
            f'Second block: {second_block}',
            flush=True,
        )
        print(
            f'Second JSON: {second_json}',
            flush=True,
        )
        print(SPACER, flush=True)

        # 2nd block copy from 2nd block JSON
        copy_block = Block.from_json(second_json)
        copy_json = copy_block.to_json()
        write_block(copy_block)

        print(
            f'Copy block: {copy_block}',
            flush=True,
        )
        print(
            f'Copy JSON: {copy_json}',
            flush=True,
        )
        print(SPACER, flush=True)

        print('Listening for new blocks', flush=True)
        while True:
            continue
