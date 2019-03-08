#!/usr/bin/env bash

echo "start.sh: called"
echo "start.sh: setting host to 127.0.0.3"

export HOST='127.0.0.3'

for dir in Expander Ranker Tiler Results; do
	echo "start.sh: Starting $dir"
	cd $dir
	python service.py &
	cd -
done

echo "start.sh: Services started"