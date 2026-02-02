#!/bin/sh
# Deletes archived and rotated log files from /var/log to free up space.
# It targets .old, .gz, and .1 files.
echo "yes mr, ninja sir, deleting old logs..."
sudo find /var/log -type f -name "*.old" -exec rm -f {} \;
sudo find /var/log -type f -name "*.gz" -exec rm -f {} \;
sudo find /var/log -type f -name "*.1" -exec rm -f {} \;