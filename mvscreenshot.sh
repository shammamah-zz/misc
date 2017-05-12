#!/bin/bash 

REC=`ls -rt ~/Documents/screenshots/Screen\ Shot*.png | tail -n 1`
cp "$REC" "$PWD"'/'$1'.png'

