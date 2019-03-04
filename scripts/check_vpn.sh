#!/bin/bash

ping -c 1 192.168.50.1 >>/dev/null
if [ $? -eq 0 ]; then
	echo "VPN estabelecida"
	exit 0
elif [ $? -eq 1 ]; then
	echo "VPN desconectada"
	exit 2
else
	echo "Erro descoñecido"
	exit 1
fi
