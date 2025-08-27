# trans/cli.py

from trans import __app_name__, __version__
import typer
from typing import Optional

App = typer.Typer()

def _version_fun(respond : bool)  :
    if respond :
        typer.echo(
            f"{__app_name__} v{__version__}"
        )
        raise typer.Exit()

@App.callback()
def main(
    version : Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=_version_fun,
        is_eager=True
    )
) -> None : return