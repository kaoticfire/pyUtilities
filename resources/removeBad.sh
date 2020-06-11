#!/bin/bash
# shellcheck disable=SC2063

file="pass.txt"

master="passwords.txt"

echo "Combining files"
cat $1 > $file
rm -f $1
echo "Removed $1" 
cat $2 > $file
rm -f $2
"Removed $2"
cat $3 > $file
rm -f $3
"Removed $3"

echo "Removing bad characters"
grep -ax '.*' "$file" > "$master"

echo "Completed"
