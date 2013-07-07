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

## License ##

### Documentation ###

This document is licensed under the Creative Commons Attribution 3.0 Unported
License. To view a copy of this license, visit
[this web page](http://creativecommons.org/licenses/by/3.0) or send a letter to
Creative Commons, 444 Castro Street, Suite 900, Mountain View, California,
94041, USA.

### Source/Binary ##

The license for all the other files in this project is as follows:

Copyright (c) 2013, Jim Turner.  All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
