#!/bin/bash
# testing multiple commands in the then section
#
testuser=yhy
#
if grep $testuser /etc/passwd; then
	echo "this is my first command"
	echo "this is my second command"
	echo "I can even put in other command besides echo:"
	ls -a /home/$testuser/.b*
else
	echo "the user $testuser does not exist on this system."
fi
