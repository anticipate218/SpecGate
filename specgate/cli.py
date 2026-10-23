"""Command line for listing and downloading modules."""

import argparse
import json
import sys

from specgate.registry import available_modules, download_modules, module_status

_COLORS = {
    "sep": "\033[38;5;220m",
    "bias_correct": "\033[38;5;43m",
    "mse": "\033[38;5;75m",
    "tta": "\033[38;5;209m",
    "pamr": "\033[38;5;183m",
}
_RESET = "\033[0m"


def _paint(name):
    if not sys.stdout.isatty():
        return name
    return f"{_COLORS.get(name, '')}{name}{_RESET}"


def main(argv=None):
    parser = argparse.ArgumentParser(prog="specgate")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="show the module catalog")
    sub.add_parser("status", help="show bundled and downloaded modules")

    p_dl = sub.add_parser("download", help="copy modules into ~/.specgate/modules")
    p_dl.add_argument("names", nargs="+", help="module ids, e.g. sep pamr")

    args = parser.parse_args(argv)
    if args.cmd == "list":
        for name, desc in available_modules().items():
            print(f"{_paint(name):s}{' ' * max(1, 14 - len(name))}{desc}")
        return 0
    if args.cmd == "status":
        print(json.dumps(module_status(), indent=2))
        return 0
    if args.cmd == "download":
        paths = download_modules(args.names)
        for path in paths:
            print(path)
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
