import argparse
from dwonloder import *
import pretty_errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="corama", description="Download a YouTube video."
    )
    parser.add_argument("subject", help="the subject to be summarized from wikipedia")
    parser.add_argument("-p", "--path", help="Output path for the content", default=".")
    args = parser.parse_args()
    summary(args.subject, args.path)
