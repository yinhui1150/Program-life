#!/bin/bash
#Testing nested ifs
#
testuser=yhh
if grep $testuser /etc/passwd; then
	echo "the user $testuser exists on this system"
else
	echo "the user $testuser does not exist this system"
	if ls -d /home/$testuser; then
		echo "however, $testuser has a directory"
	else 
		echo "$testuser has not a directory"
	fi
fi
