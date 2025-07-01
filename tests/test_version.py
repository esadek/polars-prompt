from re import fullmatch

from polars_prompt import __version__


def test_version():
    assert fullmatch(r"^\d+\.\d+\.\d+$", __version__)
