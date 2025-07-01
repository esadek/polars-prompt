from polars_prompt.main import HELP_MESSAGE, handle_dot_command


def test_handle_dot_command_help(capsys):
    local_vars = {}
    result = handle_dot_command(".help", local_vars)
    captured = capsys.readouterr()
    assert HELP_MESSAGE.strip() in captured.out
    assert result is False


def test_handle_dot_command_exit():
    local_vars = {}
    assert handle_dot_command(".exit", local_vars)
    assert handle_dot_command(".quit", local_vars)


def test_handle_dot_command_vars_empty(capsys):
    local_vars = {}
    result = handle_dot_command(".vars", local_vars)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert result is False


def test_handle_dot_command_vars_nonempty(capsys):
    local_vars = {"foo": 123, "bar": "baz"}
    result = handle_dot_command(".vars", local_vars)
    captured = capsys.readouterr()
    assert "foo = 123" in captured.out
    assert "bar = 'baz'" in captured.out
    assert result is False


def test_handle_dot_command_unknown():
    local_vars = {}
    assert handle_dot_command(".unknown", local_vars) is False
