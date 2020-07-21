from .utils import sha256, block_bytes


class Header:
    """
    Header should have immutable members:
    - block number
    - hash of previous block
    """
    def __init__(self, number: int, previous_hash: str):
        self._number = number
        self._previous_hash = previous_hash

    @property
    def number(self) -> int:
        return self._number

    @property
    def previous_hash(self) -> str:
        return self._previous_hash


class Body:
    """
    Body should have immutable list of string elements
    """
    def __init__(self, data: tuple):
        self._data = data

    @property
    def data(self) -> tuple:
        return self._data

    def __str__(self):
        return str(self._data)


class Block:
    buffer = []

    def __init__(self, number: int, previous_hash: str):
        self._header: Header = Header(
            number=number,
            previous_hash=previous_hash,
        )
        self._body: Body = Body(
            data=tuple(Block.buffer.copy()),
        )
        self._hash = None
        Block.buffer = []

    @classmethod
    def append(cls, element: str):
        cls.buffer.append(element)

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        return self._body

    def hash(self):
        if self._hash:
            return self._hash
        else:
            self._hash = sha256(block_bytes(block=self))
            return self._hash

    def __str__(self):
        return (
            f'Number: {self._header.number} '
            f'Previous hash: {self._header.previous_hash} '
            f'Body: {self.body} '
            f'Hash: {self.hash()}'
        )
