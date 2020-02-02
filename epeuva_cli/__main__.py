import click
import logging

from epeuva_cli.cli import epeuva
import epeuva_cli.cli.app.cmd
import epeuva_cli.cli.base.cmd
import epeuva_cli.cli.image.cmd
import epeuva_cli.cli.job.cmd
import epeuva_cli.cli.label.cmd
import epeuva_cli.cli.model.cmd
import epeuva_cli.cli.task.cmd
import epeuva_cli.utils.config
from epeuva_cli.utils.output_handler import output


logger = logging.getLogger(__name__)


def main():
    epeuva.cli()


if __name__ == '__main__':
    main()
