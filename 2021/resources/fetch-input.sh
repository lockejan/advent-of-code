#!/usr/bin/env sh

SESSION=$1
LEVEL=$2
YEAR=${3:-2021}

curl -b session=${SESSION} https://adventofcode.com/${YEAR}/day/${LEVEL}/input >input-test-${2}.txt
