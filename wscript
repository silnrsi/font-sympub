#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

DOCDIR = ["documentation", "web"]

APPNAME = 'SymPub'
DESC_SHORT = "SymPub Font"

# build primary font
getufoinfo('source/masters/SymPub-Regular.ufo')

cmds = [
    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    ]

designspace('source/SymPub.designspace',
            target = process("${DS:FILENAME_BASE}.ttf", *cmds),
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = f'../source/SymPub-WOFF-metadata.xml')
)
