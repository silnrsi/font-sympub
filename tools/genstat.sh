#!/bin/sh

SRC="$1"
TGT="$2"
cp -v "$SRC" "$TGT"
gftools gen-stat --inplace "$TGT"
gftools fix-family --inplace --rename-family="SymPub TestA" "$TGT"
