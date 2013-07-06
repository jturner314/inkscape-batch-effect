SHELL = /bin/bash

.PHONY: all install clean

all:

install:
	install -d "$(HOME)/.config/inkscape/extensions/"
	install batch-effect.py -t "$(HOME)/.config/inkscape/extensions/"
	install batch-effect.inx -t "$(HOME)/.config/inkscape/extensions/"

clean:
	$(RM) *.py[cod]
