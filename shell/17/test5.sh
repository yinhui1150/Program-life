#!/bin/bash
# using the return commadn in a function

function db1 {
    read -p "Enter a value :" value
    echo "double the value"
    return $[ $value * 2 ]

}

db1
echo "The new value is $?"
