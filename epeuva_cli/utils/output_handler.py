import json

import click
from pygments import highlight, lexers, formatters


class OutputHandler():
    def __init__(self, debug=False, pretty=False):
        self._debug = debug
        self._pretty = pretty

    def set(self, debug, pretty):
        self._debug = debug
        self._pretty = pretty

    def print(self, obj):
        content = obj

        if self._pretty:
            if isinstance(obj, dict) or isinstance(obj, list):
                content = self.prettify(obj, color=True)
            elif isinstance(obj, str):
                try:
                    content = self.colorize_json(obj)
                except Exception:
                    pass

        click.echo(content)

    def debug(self, obj):
        if self._debug:
            self.print(obj)

    def colorize_json(self, json_str):
        return highlight(
            json_str,
            lexers.JsonLexer(),
            formatters.TerminalFormatter()
        )

    def prettify(self, obj, color=False):
        json_str = json.dumps(obj, indent=2, sort_keys=True)
        if color:
            json_str = self.colorize_json(json_str)
        return json_str


output = OutputHandler()
