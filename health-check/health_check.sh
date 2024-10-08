#!/bin/bash

TIME=$(date)

echo "$TIME [begin probe check]" >> /root/health_check.log

if netstat -tuln | grep -q "3000"; then
    echo "$TIME INFO Port 3000 is running" >> /root/health_check.log
	echo "$TIME [end probe check]" >> /root/health_check.log
else
    echo "$TIME WARN Port 3000 is not running" >> /root/health_check.log
	echo "$TIME [end probe check]" >> /root/health_check.log
    exit 1
fi

