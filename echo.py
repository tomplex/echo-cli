__author__ = 'tom caruso'

import os

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from click import echo

from utils import ensure_path_exists


def main():
    user_home = os.environ.get('HOME', '')
    echo_path = f"{user_home}/.echo"
    ensure_path_exists(echo_path)

    while True:
        try:
            user_input = prompt('echo==> ',
                                history=FileHistory(f'{echo_path}/echo-history'),
                                auto_suggest=AutoSuggestFromHistory()
                                )
            echo(user_input)
        except KeyboardInterrupt:
            exit(0)


if __name__ == "__main__":
    main()
