Inkscape Batch Effect
=====================

This script allows for batch execution of Inkscape extensions.  Based on a .csv
file listing the executables and options, it chains together extensions into a
pipeline that acts like a single Inkscape extension.

## Installation ##

### Linux ###

Execute the following:

    # make install

This will install the necessary files into `/usr/share/inkscape/extensions/`.

### Windows ###

Copy `batch_effect.py` and `batch_effect.inx` into `C:\Program
Files\Inkscape\share\extensions\`.  Note that although I designed this extension
to be portable, it is untested on Windows.

## Usage ##

After installation, you should be able to run the extension in Inkscape from the
menu item Extensions > Render > Batch Effect...  You only need to supply a path
to the .csv file listing the executables and arguments to call.  See
**Operation** for more information about this file.

## Operation ##

This extension takes as input the path to a single .csv file listing the
executables to be called and their arguments.  The first column should list the
absolute paths to the executables.  The remaining columns should list the
options/arguments.  For example:

    /usr/share/inkscape/extensions/gears.py,-t,50,-p,10,-a,20
    /usr/share/inkscape/extensions/gears.py,-t,20,-p,20,-a,30

Note that if `batch_effect.py` receives any `--id` arguments from Inkscape, then
it inserts these unmodified at the beginning of the argument list of each call.

`batch_effect.py` operates by passing the SVG data provided by Inkscape to the
first executable on stdin.  It then pipes stdout from that executable to stdin
on the next executable, and so on.  The stdout from the final executable is
piped to the stdout of `batch_effect.py`, which Inkscape receives.

To determine the executables and the appropriate arguments for Inkscape
extensions, read the source files in the directory where your extensions are
stored.  In particular, .inx files describe the executables and arguments for
every extension.  They define the interface that Inkscape uses to execute the
extensions.  See
[this wiki page](http://wiki.inkscape.org/wiki/index.php/Script_extensions) for
more information about how Inkscape extensions work.
