#!/bin/bash
# testing string equality
testuser=rich

if [ $USER != $testuser ]; then
	echo "this is not $testuser"
else
	echo "welcome $testuser"
fi
