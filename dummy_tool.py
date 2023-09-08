#!/usr/bin/env python3

import argparse
import os


################################################################################

def setup_argument_parser():
    """Setup argparse parser."""
    help_description = """
    Dummy tool.
    """
    # Define argument parser.
    p = argparse.ArgumentParser(add_help=False,
                                prog="dummy_tool.py",
                                description=help_description,
                                formatter_class=argparse.MetavarTypeHelpFormatter)

    # Required arguments.
    p.add_argument("-h", "--help",
                   action="help",
                   help="Print help message")
    p.add_argument("--in",
                   dest="in_file",
                   type=str,
                   metavar='str',
                   required=True,
                   help="Input file")
    p.add_argument("--ids",
                   dest="in_ids",
                   type=str,
                   metavar='str',
                   nargs='+',
                   required=True,
                   help="List of IDs (--ids id1 id2 .. )")
    p.add_argument("--out",
                   dest="out_folder",
                   type=str,
                   metavar='str',
                   required=True,
                   help="Results output folder")
    p.add_argument("--turn-on",
                   dest="turn_me_on",
                   default=False,
                   action="store_true",
                   help="Turn me on (default: False)")
    return p

################################################################################


if __name__ == '__main__':

    parser = setup_argument_parser()
    args = parser.parse_args()

    assert os.path.exists(args.in_file), "--in file \"%s\" not found" % (args.in_file)

    if not os.path.exists(args.out_folder):
        os.makedirs(args.out_folder)

    for in_id in args.in_ids:
        print("Input ID:", in_id)

    if args.turn_me_on:
        print("Now I'm turned on ... ")

    in_bed = ""
    out_file = args.out_folder + "/out_file.txt"

    OUT = open(out_file, "w")
    OUT.write("this is dumb\n")
    OUT.close()