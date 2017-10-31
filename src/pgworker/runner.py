import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='pgworker',
        description='A distributed process worker using the builtin Postgres notification system', )

    parser.add_argument('-v', '--verbose', action='count')

    subparsers = parser.add_subparsers(title='commands')

    parser_run = subparsers.add_parser('run', help='Run the servicer worker') # type: argparse.ArgumentParser
    parser_run.add_argument('--name', help='Worker name, by default uses the hostname')

    parser_inspect = subparsers.add_parser('inspect', help='Inspect running worker')
    parser_inspect.add_argument('--detailed', help='Detailed output')

    options = parser.parse_args()

    parser.print_help()
