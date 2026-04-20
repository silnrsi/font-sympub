#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

DOCDIR = ["documentation", "web"]

APPNAME = 'SymPub'
DESC_SHORT = "SymPub Font"

# build primary font
getufoinfo('source/SymPub-Regular.ufo')

designspace('source/SymPub.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = f'../source/SymPub-WOFF-metadata.xml')
)
