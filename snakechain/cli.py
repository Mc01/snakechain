import typer

from snakechain.blockchain import Blockchain, Block


app = typer.Typer()


@app.command()
def start_node():
    Blockchain().start_node()


@app.command()
def add_element(element: str):
    Blockchain().append_element(element)
    typer.echo(f'Added element to buffer: {element}')


@app.command()
def create_block():
    new_block: Block = Blockchain().create_block()
    typer.echo(f'Created block from buffer: {new_block.header.number}')


@app.command()
def get_block(number: int):
    pass


@app.command()
def get_element(number: int):
    pass


@app.command()
def get_statistics():
    pass


if __name__ == '__main__':
    app()
