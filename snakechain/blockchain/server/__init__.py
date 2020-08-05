from grpclib.utils import graceful_exit

from .base import NodeBase, GRPCServer


class Node(NodeBase):
    async def hello(self, stream):
        request = await stream.recv_message()
        message = f"Hello, {request.name}!"
        await stream.send_message(
            # hello_reply(message=message)
        )

    async def append_element(self, stream):
        request = await stream.recv_message()
        await stream.send_message

    async def server(self, host="127.0.0.1", port=8001):
        server = GRPCServer([self])
        with graceful_exit([server]):
            await server.start(host, port)
            print(f"Serving on {host}:{port}")
            await server.wait_closed()
