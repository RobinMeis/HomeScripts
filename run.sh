#!/bin/bash
#This script is gonnas to be called by a cronjob and calls the home automation scripts

cd "$(dirname "$0")" #Set working directory (important for running cronjobs)

python3 aseag2mqtt.py
