import json
from typing import List

from .body import Body
from .header import Header
from ..utils import sha256, block_bytes


class Block:
    def __init__(
            self,
            number: int,
            previous_hash: str,
            data: List[str] = None,
    ):
        self._header: Header = Header(
            number=number,
            previous_hash=previous_hash,
        )
        self._body: Body = Body(data=tuple(data))
        self._hash: str = ''

    @property
    def header(self) -> Header:
        return self._header

    @property
    def body(self) -> Body:
        return self._body

    @property
    def hash(self) -> str:
        if self._hash:
            return self._hash
        else:
            self._hash = sha256(block_bytes(
                block=self,
            ))
            return self._hash

    @property
    def __dict__(self) -> dict:
        return {
            **self._header.__dict__,
            **self._body.__dict__,
        }

    def __str__(self) -> str:
        return (
            f'Block - '
            f'{self._header} '
            f'{self._body} '
            f'Hash: {self.hash}'
        )
