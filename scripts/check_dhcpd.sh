#!/bin/bash

systemctl status dhcpd

if [ $? -eq 0 ]; then
	exit 0
else
	exit 2
fi
