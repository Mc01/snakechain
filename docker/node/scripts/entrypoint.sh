#!/usr/bin/env bash
echo ":: SnakeChain Up ::"
/scripts/./formatter.sh
/scripts/./compile_proto.sh
/scripts/./wait_for_storage.sh
python cli.py start-node
echo ":: SnakeChain Down ::"
