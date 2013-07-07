SHELL = /bin/bash

.PHONY: all install clean

all:

install:
	install -d "$(DESTDIR)/usr/share/inkscape/extensions/"
	install batch_effect.py -t "$(DESTDIR)/usr/share/inkscape/extensions/"
	install batch_effect.inx -m 644 -t "$(DESTDIR)/usr/share/inkscape/extensions/"

clean:
	$(RM) *.py[cod]
