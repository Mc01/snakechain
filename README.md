# SnakeChain

Blockchain engine implementation in Python

## Setup

```
docker-compose up -d
```

## Usage

```
docker-compose exec node ./cli.py $command
```

> Note: Where `$command` is one of following:
> - add-element
> - create-block
> - get-block
> - get-element
> - get-statistics

## Environment

Following environment variables are mandatory (defined in `docker-compose.yml`):
- `BUFFER_HOST`
- `BUFFER_PORT`
- `STORAGE_HOST`
- `STORAGE_USER`
- `STORAGE_PASSWORD`

Following environment variables are optional and have defaults:
- `STORAGE_BUCKET` (default value: `default`)
- `NUMBER_OF_BLOCKS_IN_MEMORY` (default value: `10`)
- `SPACER` (default value: `------*------*------*------*------*------`)

## Design

SnakeChain core elements are following:
- CLI
> Executes commands on blockchain node
- Node
> Listens for CLI commands 
- Buffer
> Keeps recent blocks and next block elements in RAM
- Storage
> Stores all blocks on Disk

## TODO checklist
- Add unit tests
- Make use of black formatter
- Introduce gRPC between CLI and Node
- Use AsyncIO for Node and integrate with other components
- Make more intelligent hashing (introduce Merkle Trees for example)
- Add more crypto features (simple consensus like pBFT for example)
- Add support for P2P broadcasting

## Packages

Following packages used across project:
- [CLI - typer](https://github.com/tiangolo/typer)
- [gRPC - betterproto](https://github.com/danielgtaylor/python-betterproto)
- [Buffer - redis](https://github.com/andymccurdy/redis-py)
- [Storage - couchbase](https://github.com/couchbase/couchbase-python-client)
- [Formatter - black](https://github.com/psf/black)
