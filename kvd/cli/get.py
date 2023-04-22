from kvd.cli import cli, get_host

import click
import httpx

@cli.command()
@click.argument("name")
def get(name: str):
    response = httpx.get(f'{get_host()}/{name}')
    click.echo(response.text)
