import typer

from blockchain import Blockchain


app = typer.Typer()


@app.command()
def start_node():
    Blockchain().start_node()


@app.command()
def add_element():
    typer.echo('Adding element to blockchain')


@app.command()
def create_block():
    typer.echo('Creating block from buffer')


if __name__ == '__main__':
    app()
