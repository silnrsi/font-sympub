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
    cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
    ]

designspace('source/SymPub.designspace',
            target = process("${DS:FILENAME_BASE}.ttf", *cmds),
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = f'../source/SymPub-WOFF-metadata.xml')
)

variable = package(
    appname = APPNAME + '-variable',
    version = VERSION,
    docdir = {'documentation': 'documentation', 'variable/web': 'web'}
)

stem = APPNAME
font(target = process(f'variable/{stem}.ttf',
    cmd('gftools fix-font --include-source-fixes -o ${TGT} ${DEP}'),
    cmd('../tools/genstat.sh ${DEP} ${TGT}')
    ),
    source = f'source/variable/{stem}.designspace',
    params = '--feature-writer None --filter DecomposeTransformedComponentsFilter',
    version = VERSION,
    woff = woff(f'variable/web/{stem}.woff2', type='woff2',
        metadata = f'../source/{APPNAME}-WOFF-metadata.xml',
        dontship = True),
    package = variable,
    no_test = True
)
