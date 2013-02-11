#! /bin/bash

# Make a flat list of words, separated by newlines, from a text file

file=$1
cat $1 | sed "s/\s/\n/g" | grep "\w" | sed "s/\W//g" > $1.word-list

