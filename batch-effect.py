#!/usr/bin/env python

import argparse
import csv
import shutil
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chain together Inkscape extensions")
    parser.add_argument('--id', type=str, action='append', dest='ids', default=[],
                        help="id attribute of object to manipulate")
    parser.add_argument('--csvpath', type=str, required=True,
                        help="Path to .csv file containing command lines")
    parser.add_argument('svgpath', type=str, nargs='?', default='',
                        help="Path to temporary SVG file to use for input to the first extension")
    args = parser.parse_args()

    with open(args.csvpath, 'rb') as f:
        # Make an argument list of the ids
        id_args = []
        for id in args.ids:
            id_args.extend(('--id', id))
        # Take input for the first call from temporary file or stdin
        if args.svgpath:
            stream = open(args.svgpath)
        else:
            stream = sys.stdin
        # Execute all the calls
        for row in csv.reader(f):
            # Insert the ids into the call
            call = row[:1] + id_args + row[1:]
            # Make the call
            p = subprocess.Popen(call, stdin=stream, stdout=subprocess.PIPE)
            # Close our handle to the input pipe because we no longer need it
            stream.close()
            # Grab the output pipe for input into the next call
            stream = p.stdout
        # Send output from last call on stdout
        shutil.copyfileobj(stream, sys.stdout)
