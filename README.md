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

Following environment variables are mandatory:
- `REDIS_HOST`
- `REDIS_PORT`

Following environment variables are optional and have defaults:
- `NUMBER_OF_BLOCKS_IN_MEMORY` (default value: `10`)
- `BLOCKCHAIN_STORAGE_FILE` (default value: `storage/ledger.json`)
- `SPACER` (default value: `------*------*------*------*------*------`)

## Design

### CLI

### gRPC

### Node

### Cache

### Database

### Hashing

### Integrity

### Formatter

## Packages

Following packages used across project:
- [CLI - typer](https://github.com/tiangolo/typer)
- [gRPC - betterproto](https://github.com/danielgtaylor/python-betterproto)
- [Cache - redis](https://github.com/andymccurdy/redis-py)
- [Database - couchbase](https://github.com/couchbase/couchbase-python-client)
- [Formatter - black](https://github.com/psf/black)
