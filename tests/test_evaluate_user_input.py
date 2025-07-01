from pytest import fixture

from polars_prompt.main import evaluate_user_input


@fixture
def local_vars():
    return {}


def test_eval_expression_prints_result(capsys, local_vars):
    evaluate_user_input("1 + 2", local_vars)
    captured = capsys.readouterr()
    assert "3" in captured.out


def test_eval_expression_none_result(capsys, local_vars):
    evaluate_user_input("print('hello')", local_vars)
    captured = capsys.readouterr()
    assert "hello" in captured.out


def test_exec_statement_assigns_variable(local_vars):
    evaluate_user_input("x = 42", local_vars)
    assert local_vars["x"] == 42


def test_exec_statement_raises_exception(capsys, local_vars):
    evaluate_user_input("raise ValueError('fail')", local_vars)
    captured = capsys.readouterr()
    assert "ValueError: fail" in captured.out


def test_eval_with_polars_available(capsys, local_vars):
    evaluate_user_input("pl.DataFrame({'a': [1,2]})", local_vars)
    captured = capsys.readouterr()
    assert "shape:" in captured.out or "a" in captured.out
