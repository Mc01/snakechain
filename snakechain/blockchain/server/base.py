import abc
from typing import Dict

from grpclib.const import Handler
from grpclib.server import Server

from .typing import InterfaceServable, InterfaceClosable


class NodeBase(abc.ABC, InterfaceServable):
    @abc.abstractmethod
    async def hello(self, stream: '') -> None:
        pass

    # noinspection PyMethodMayBeStatic
    def __mapping__(self) -> Dict[str, Handler]:
        return {
            '': Handler(
            ),
        }


class GRPCServer(Server, InterfaceClosable):
    pass
