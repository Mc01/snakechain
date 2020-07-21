from .block import Block


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
        self.previous_block_hash = new_block.hash()
        self.next_block_number += 1
        return new_block

    def start_node(self):
        print('Starting blockchain node', flush=True)

        self._append_element(element='one')
        self._append_element(element='two')
        first = self._create_block()

        self._append_element(element='three')
        self._append_element(element='four')
        second = self._create_block()

        print(first, flush=True)
        print(second, flush=True)
        print('Debug')

        while True:
            continue
