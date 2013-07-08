#!/usr/bin/env python

import csv
import optparse
import shutil
import subprocess
import sys

if __name__ == '__main__':
    parser = optparse.OptionParser(description="Chain together Inkscape extensions",
                                   usage="%prog [options] svgpath")
    parser.add_option('--id', dest='ids', action='append', type=str, default=[],
                      help="ID attributes of objects to manipulate. Passed to all extensions.")
    parser.add_option('--csvpath', dest='csvpath', type=str,
                      help="Path to .csv file containing command lines")
    options, args = parser.parse_args()

    with open(options.csvpath, 'rb') as f:
        # Make an argument list of the ids
        id_args = []
        for id in options.ids:
            id_args.extend(('--id', id))
        # Take input for the first call from temporary file or stdin
        if args:
            stream = open(args[0])
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
