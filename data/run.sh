#!/bin/bash
set -e

cargo build --release
cp ../target/release/chem-matcher .


# FILE_PATHS=$(find . -name "chunk*.gz" | sort | sed 's|\./||g')
# ./chem-matcher  -c ../../../Data/CID-Synonym-filtered \
#                 -f $FILE_PATHS \
#                 -o output.csv

# ./chem-matcher  -c ../../../Data/test_map2 \
# ./chem-matcher  -c ../../../Data/CID-SMILES-Synonyms \
./chem-matcher  -c ../../../Data/CID-Synonym-filtered \
                -f chunk1.gz \
                -o output.csv --stop 2000
