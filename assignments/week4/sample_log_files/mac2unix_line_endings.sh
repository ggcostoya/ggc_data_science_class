#!/bin/bash
for file in $@; do
cat $file | tr '\r' '\n' > unix_$file
done