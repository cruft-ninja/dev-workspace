#!/bin/sh
# Prunes all unused docker images from the system.
# -a: Remove all unused images, not just dangling ones.
# -f: Do not prompt for confirmation.
docker image prune -a -f