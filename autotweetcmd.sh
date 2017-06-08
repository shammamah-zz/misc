#!/bin/bash

export PATH="/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin"

$(cat ~/.bash_history | tail -r -100 > ~/Documents/scripts/hist.txt)
CMD=""
while [[ "${#CMD}" -lt 1 ]]; do
	LN=$(( (RANDOM%100) +1 ))
	CMD=$(tail -"$LN" ~/Documents/scripts/hist.txt | head -1)
done 

t update "$CMD"
echo -e "Just tweeted \"$CMD\".\n"

