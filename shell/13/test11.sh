#!/bin/bash
# changing the IFS value

IFS.OLD=$IFS
for entry in $(cat /etc/passwd)
do 
    IFS=$'\n'
    echo "Values in $entry -"
    IFS=:
    for Value in $entry
    do
    echo "  $Value"
    done
done
