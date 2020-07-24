from __future__ import annotations

from typing import TYPE_CHECKING

from ..exceptions import IntegrityError

if TYPE_CHECKING:
    from ..block import Block


class IntegrityCheck:
    def __init__(self, genesis_block: Block):
        self.current_block: Block = genesis_block

    def validate_block(self, latest_block: Block):
        if self.current_block.hash != latest_block.header.previous_hash:
            raise IntegrityError(
                previous_block=self.current_block,
                current_block=latest_block,
            )

        self.current_block = latest_block
