import json
from typing import Optional, List

from redis import Redis

from ..config import BUFFER_HOST, BUFFER_PORT


class Buffer:
    def __init__(self):
        self.redis = Redis(host=BUFFER_HOST, port=BUFFER_PORT,)

    @staticmethod
    def _get_block_key(number):
        return f"b{number}"

    def _get_value(self, key) -> Optional:
        raw_data = self.redis.get(name=key)
        return json.loads(raw_data) if raw_data else None

    def _set_value(self, key, value):
        raw_data = json.dumps(value)
        self.redis.set(name=key, value=raw_data)

    def add_body_element(self, block_number: int, body_element: str):
        block_key = self._get_block_key(number=block_number)
        existing_elements = self._get_value(key=block_key)

        if existing_elements:
            new_elements = existing_elements + [body_element]
        else:
            new_elements = [body_element]

        self._set_value(block_key, new_elements)

    def get_body(self, block_number: int) -> List[str]:
        block_key = self._get_block_key(number=block_number)
        return self._get_value(key=block_key)

    def remove_body(self, block_number: int):
        block_key = self._get_block_key(number=block_number)
        self.redis.delete(block_key)
