#!/bin/bash

echo "<!DOCTYPE html>" > myList.html
echo "<html>" >> myList.html
echo "<body>" >> myList.html
echo "<h1>" >> myList.html
echo "$(pwd)" >> myList.html
echo "</h1>" >> myList.html

for f in $( ls -1);
do
	echo "$f" >> myList.html
	echo "</br>" >> myList.html
done

echo "</body>" >> myList.html
echo "</html>" >> myList.html
xdg-open myList.html
