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
- `REDIS_HOST`
- `REDIS_PORT`
- `STORAGE_HOST`
- `STORAGE_USER`
- `STORAGE_PASSWORD`

Following environment variables are optional and have defaults:
- `NUMBER_OF_BLOCKS_IN_MEMORY` (default value: `10`)
- `SPACER` (default value: `------*------*------*------*------*------`)

## Design

SnakeChain core elements are following:
- CLI
- Node
- Buffer
- Storage

### CLI

### gRPC

### Node

### Buffer

### Storage

### Hashing

### Integrity

### Formatter

## Packages

Following packages used across project:
- [CLI - typer](https://github.com/tiangolo/typer)
- [gRPC - betterproto](https://github.com/danielgtaylor/python-betterproto)
- [Buffer - redis](https://github.com/andymccurdy/redis-py)
- [Storage - couchbase](https://github.com/couchbase/couchbase-python-client)
- [Formatter - black](https://github.com/psf/black)
