from os import environ
from kvd.content import assume_file_content_type, assume_text_content_type

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
@click.argument("name")
@click.option("--value", "-v")
@click.option("--file", "-f")
def upload(name: str, value: str, file: str):
    if value is None and file is None or value is not None and file is not None:
        raise click.UsageError("Either --value or --file must be specified")

    content_type = None
    data = None

    if file is not None:
        content_type = assume_file_content_type(file)
        with open(file, "rb") as f:
            data = f.read()

    if value is not None:
        content_type = assume_text_content_type(value)
        data = value.encode("utf-8")

    response = httpx.post(
        f'{get_host()}/uploads/{name}',
        data=data,
        headers={'Content-Type': content_type}
    )
    click.echo(response.text)


@cli.command()
@click.argument("name")
def get(name: str):
    response = httpx.get(f'{get_host()}/uploads/{name}')
    click.echo(response.text)

@cli.command()
@click.argument("name")
def delete(name: str):
    response = httpx.delete(f'{get_host()}/uploads/{name}')
    click.echo(response.text)

if __name__ == '__main__':
    cli()
