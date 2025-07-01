import polars as pl
from prompt_toolkit import PromptSession
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers.python import PythonLexer
from pygments.styles import get_style_by_name

from polars_prompt import __version__

HELP_MESSAGE = """Key Bindings:
enter        add newline
meta+enter   submit input
esc, enter   submit input
ctrl+d       exit prompt

Dot Commands:
.help        usage hints
.vars        local variables
.exit        exit prompt
.quit        exit prompt"""


def handle_dot_command(cmd: str, local_vars: dict) -> bool:
    if cmd in [".exit", ".quit"]:
        return True
    elif cmd == ".help":
        print(HELP_MESSAGE)
    elif cmd == ".vars":
        if local_vars:
            for key, value in local_vars.items():
                print(f"{key} = {value!r}")
    return False


def evaluate_user_input(user_code: str, local_vars: dict) -> None:
    try:
        result = eval(user_code, {"pl": pl}, local_vars)
        if result is not None:
            print(result)
    except Exception:
        try:
            exec(user_code, {"pl": pl}, local_vars)
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")


def main() -> None:
    print(f'Polars Prompt v{__version__}\nEnter ".help" for usage hints.')

    session = PromptSession(
        multiline=True,
        lexer=PygmentsLexer(PythonLexer),
        style=style_from_pygments_cls(get_style_by_name("dracula")),
        cursor=CursorShape.BEAM,
        mouse_support=True,
    )

    local_vars = {}
    while True:
        try:
            user_input = session.prompt("\n> ")
            cleaned_input = user_input.strip().lower()
            if cleaned_input.startswith("."):
                if handle_dot_command(cleaned_input, local_vars):
                    break
                continue
            evaluate_user_input(user_input, local_vars)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break


if __name__ == "__main__":
    main()
