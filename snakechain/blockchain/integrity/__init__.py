from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..exceptions import IntegrityError

if TYPE_CHECKING:
    from ..block import Block


class IntegrityCheck:
    def __init__(self):
        self.current_block: Optional[Block] = None
        self.validated_count = 0

    def validate_block(self, latest_block: Block):
        """
        Validates blocks by comparing their hash connections
        """
        if (
                self.current_block and
                self.current_block.hash != latest_block.header.previous_hash
        ):
            raise IntegrityError(
                previous_block=self.current_block,
                current_block=latest_block,
            )

        self.current_block = latest_block
        self.validated_count += 1
