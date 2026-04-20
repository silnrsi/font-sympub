#!/usr/bin/env python
__doc__ = '''Create markdown encoding table for SymPub font docs '''
__url__ = 'https://github.com/silnrsi/font-sympub'
__copyright__ = 'Copyright (c) 2023-2026 SIL Global (https://www.sil.org)'
__license__ = 'Released under the MIT License (https://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

import csv

incsv = "../source/glyph_data.csv"
outfile = "../documentation/encoding.md"
header = """# Encoded Symbols

These are the encoded characters in the SymPub fonts. The characters from the font are shown in context.

"""

def main():
    tablehead = "Image | USV | Description | Represents\n"
    tablediv  = "----- | --- | ----------- | ----------\n"
    tablerows = ""
    # read csv
    with open(incsv, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["usv"] != "" and row["in_docs"] == "D":
                fonts = ""
                newrow = "![](images/img_" + row["usv"][2:6] + ".png)" + " | " + row["usv"] + " | " + row["doc_name"] + " | " + row["doc_uni"] + "\n"
                tablerows += newrow

    table = tablehead + tablediv + tablerows

    output = open(outfile,'w')
    output.write(header)
    output.write(table)
    output.close()
    
if __name__ == "__main__": main()
