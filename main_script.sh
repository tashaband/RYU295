#!/bin/bash

for i in "/home/ubuntu/hpingScripts/"*
do
	"$i" &
done

wait
