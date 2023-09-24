#!/usr/bin/env python3
# Purpose: Say hello

import argparse


# ------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description="say hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


# ------------------------------------------------


def main():
    """Heavy lifting"""
    args = get_args()
    print("Hello, " + args.name + "!")


# ------------------------------------------------
if __name__ == "__main__":
    main()
