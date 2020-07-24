class Body:
    """
    Body should have immutable list of string elements
    """
    def __init__(self, data: tuple):
        self._data = data

    @property
    def data(self) -> tuple:
        return self._data

    @property
    def __dict__(self) -> dict:
        return {
            'data': self._data,
        }

    def __str__(self) -> str:
        return (
            f'Body: {self._data}'
        )
