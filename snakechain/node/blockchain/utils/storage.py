from __future__ import annotations

import os
from typing import TYPE_CHECKING

from ..config import BLOCKCHAIN_STORAGE_FILE

if TYPE_CHECKING:
    from ..block import Block


def write_block(block: Block, truncate=False):
    if truncate:
        mode = 'w+'
    else:
        mode = 'a+'
    with open(BLOCKCHAIN_STORAGE_FILE, mode) as f:
        f.write(f'{block.to_json()}{os.linesep}')
