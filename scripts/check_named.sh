#!/bin/bash

systemctl status named

if [ $? -eq 0 ]; then
	exit 0
else
	exit 2
fi
