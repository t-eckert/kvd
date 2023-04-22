from os import environ

import click
import httpx


def get_host() -> str:
    host = environ.get("KVD_HOST")
    if host is None:
        raise click.UsageError("Please set the host using the 'KVD_HOST' environment variable.")
    return host
    

@click.group()
def cli():
    pass



@cli.command()
def list():
    response = httpx.get(f'{get_host()}/')
    click.echo(response.text)


@cli.command()
@click.argument("name")
def delete(name: str):
    response = httpx.delete(f'{get_host()}/{name}')
    click.echo(response.text)

if __name__ == '__main__':
    cli()
