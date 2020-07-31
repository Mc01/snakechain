#!/usr/bin/env python
from typing import Optional

import typer

from blockchain import Blockchain, Block


app = typer.Typer()
blockchain = Blockchain()


@app.command()
def start_node():
    blockchain.start_node()


@app.command()
def add_element(element: str):
    blockchain.append_element(element)
    typer.echo(f"Added element to buffer: {element}")


@app.command()
def create_block():
    new_block: Block = blockchain.create_block()
    typer.echo(f"Created block from buffer: {new_block.hash}")


@app.command()
def get_block(block_hash: str):
    block: Optional[Block] = blockchain.get_block(block_hash=block_hash)
    if block:
        typer.echo(f"Retrieved block for hash {block_hash}: {block}")
    else:
        typer.echo(f"Block with hash {block_hash} does not exist")


@app.command()
def get_element(block_hash: str, number: int):
    block: Optional[Block] = blockchain.get_block(block_hash=block_hash)
    if block:
        elements = block.body.data
        if len(elements) > number:
            typer.echo(
                f"Retrieved block element for hash {block_hash} "
                f"and number {number}: {elements[number]}",
            )
        else:
            typer.echo(
                f"Block with hash {block_hash} found, "
                f"but element {number} does not exist",
            )
    else:
        typer.echo(f"Block with hash {block_hash} does not exist")


@app.command()
def get_statistics():
    typer.echo(blockchain.get_statistics())


if __name__ == "__main__":
    app()
