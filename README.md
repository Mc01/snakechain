# SnakeChain

Blockchain engine implementation in Python

## Setup

```
docker-compose up -d
```

## Design

Node module is responsible for:
- Read/write the blockchain from/to the disk
- Accept new data elements to the buffer
- Generate a new block from the buffer
- Check blockchain integrity

Rest module is responsible for:
- Get the specific block
- Get the specific element of a specific block
- Get blockchain statistics (number of blocks, total size in bytes)
