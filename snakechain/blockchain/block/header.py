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

    @property
    def __dict__(self) -> dict:
        return {
            'number': self._number,
            'previous_hash': self._previous_hash,
        }

    def __str__(self) -> str:
        return (
            f'Number: {self._number} '
            f'Hash of previous block: {self._previous_hash}'
        )
