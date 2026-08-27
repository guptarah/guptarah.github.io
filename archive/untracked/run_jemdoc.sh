#!/bin/bash

for i in `ls *.jemdoc`; do
	echo $i
	python jemdoc.py -c jemdoc.conf $i
done
