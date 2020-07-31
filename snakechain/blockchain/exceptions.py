from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .block import Block


class InitError(Exception):
    """
    Exception thrown during storage bucket init
    """


class IntegrityError(Exception):
    """
    Exception thrown during integrity check of existing blocks
    """

    def __init__(self, previous_block: Block, current_block: Block):
        super(IntegrityError, self).__init__(
            f"Inconsistent integrity check between "
            f"previous block {previous_block.header.number} and"
            f"current block {current_block.header.number}. "
            f"Hash of previous block {previous_block.hash} "
            f"does not match hash provided in current block "
            f"{current_block.hash}."
        )
