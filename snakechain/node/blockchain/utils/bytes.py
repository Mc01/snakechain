from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..block import Block


DEFAULT_ENCODING = 'utf-8'


def block_bytes(block: Block) -> bytes:
    """
    SHA256 accepts bytes with encoding UTF-8 as input
    This function generates bytes based on concatenation of:
    - current block number
    - hash of previous block
    - each element of current block body
    """
    _bytes = bytes(str(block.header.number), encoding=DEFAULT_ENCODING)
    _bytes += bytes(block.header.previous_hash, encoding=DEFAULT_ENCODING)
    for element in block.body.data:
        _bytes += bytes(element, encoding=DEFAULT_ENCODING)
    return _bytes
