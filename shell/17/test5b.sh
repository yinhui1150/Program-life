#!/bin/bash
# using the echo to return a

function db1 {
    read -p "enter a value: " value
    echo $[ $value * 2 ]
}

result=$(db1)
echo "The new value is $result"
