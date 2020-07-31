#!/usr/bin/env bash
echo ":: SnakeChain Up ::"
/./compile_proto.sh
/./wait_for_storage.sh
python cli.py start-node
echo ":: SnakeChain Down ::"
