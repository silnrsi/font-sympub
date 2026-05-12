#!/bin/bash

ar=$PWD/tools/archive/noto
glyphnames=$ar/glyph_names.csv

declare -A noto_script
noto_script[lcg]=latn
noto_script[sym]=zsym
noto_script[math]=zmlt
noto_script[sym2]=zsym

declare -A noto_ufos
noto_ufos[lcg]=''
noto_ufos[sym]=Symbols
noto_ufos[math]=Math
noto_ufos[sym2]=Symbols2

cat $ar/range.txt $ar/single.txt > $ar/import.txt

pushd source/masters
for script in lcg sym math sym2
do

    for weight in Thin Regular Black
    do
        ufo=SymPub-${weight}.ufo

        # import
        glyphs=$ar/import-${script}-${weight}.csv
        noto=$HOME/script/${noto_script[$script]}/fonts/noto-local/instances/NotoSans${noto_ufos[$script]}-${weight}.ufo
        psfgetglyphnames -i $ar/import.txt -a $glyphnames $noto $glyphs
        psfcopyglyphs --rename rename --unicode usv -s $noto -i $glyphs -l ${script}-${weight}.log $ufo

        # check
        composites -c $ufo
        ls -l $ufo/glyphs/*copy?.glif

        # colors
        psfsetmarkcolors -i $ar/range.txt -u -c g_dark_gray $ufo
        psfsetmarkcolors -i $ar/single.txt -u -c g_dark_green $ufo
    done
done
popd

# glyph data
ufo2glyphdata $HOME/script/adobe/agl-aglfn/aglfn.txt source/masters/*-Regular.ufo source/gd.csv
