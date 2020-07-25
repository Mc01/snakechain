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
> - add_element
> - create_block
> - get_block
> - get_element
> - get_statistics

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
