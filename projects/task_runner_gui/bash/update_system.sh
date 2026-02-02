#!/bin/bash
# Performs a full system update using apt-get.
# Includes updating package lists, upgrading packages, and removing unnecessary dependencies.
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y