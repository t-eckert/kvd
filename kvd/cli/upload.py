from kvd.cli import cli, get_host
from kvd.content import assume_file_content_type, assume_text_content_type

import click
import httpx

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
        data=data, # type: ignore
        headers={'Content-Type': content_type}
    )
    click.echo(response.text)
