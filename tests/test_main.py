from unittest.mock import patch

from polars_prompt import __version__
from polars_prompt.main import main


def test_start_messages(capsys):
    with patch("prompt_toolkit.PromptSession.prompt", side_effect=EOFError):
        main()
    out = capsys.readouterr().out
    assert f"Polars Prompt v{__version__}" in out
    assert 'Enter ".help" for usage hints.' in out


def test_dataframe(capsys):
    inputs = iter(['df = pl.DataFrame({"name": ["Tom"], "age": [24]})', "df.shape", ".quit"])
    with patch("prompt_toolkit.PromptSession.prompt", side_effect=lambda _: next(inputs)):
        main()
    out = capsys.readouterr().out
    assert "(1, 2)" in out
