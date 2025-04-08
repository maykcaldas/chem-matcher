#!/bin/bash
set -e

cargo build --release
cp ../target/release/chem-matcher .


FILE_PATHS=$(find . -name "chunk*.gz" | sort | sed 's|\./||g')
# ./chem-matcher  -c ../../../Data/CID-Synonym-filtered \
#                 -f $FILE_PATHS \
#                 -o s2orc.csv

./chem-matcher  -c ../../../Data/CID-SMILES-Synonyms \
                -f $FILE_PATHS \
                -o s2orc.csv
