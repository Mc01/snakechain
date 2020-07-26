#!/usr/bin/env bash
echo ":: SnakeChain Up ::"
/./wait_for_storage.sh
python cli.py start-node
echo ":: SnakeChain Down ::"
