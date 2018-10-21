#!/bin/bash
# adding values in an array

function addarray {
    local sum=0
    local newarray
    newarray=($(echo "$@"))
    for value in ${newarray[*]}
    do
        sum=$[ $sum + $value ]
    done
    echo $sum
}

myarray=(1 2 3 4 5)
echo "The origin array is: ${myarray[*]}"
addarray ${myarray[*]}
