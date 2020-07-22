from __future__ import annotations

from typing import TYPE_CHECKING

from ..config import BLOCKCHAIN_STORAGE_FILE

if TYPE_CHECKING:
    from ..block import Block


def write_block(block: Block):
    with open(BLOCKCHAIN_STORAGE_FILE) as f:
        f.write(str(block))
