from typing import Optional
import typer
comm = typer.Typer(help="Awesome CLI user manager.")

@comm.command()
def name(name: Optional[str]=None):
    typer.echo(f"Hello {name}")


@comm.command()
def goodbye(name: Optional[str]=None, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    comm()