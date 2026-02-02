#!/bin/bash
# user_list.sh: Generates a summary of human users on the system.
#
# This script parses /etc/passwd to find users with a UID of 1000 or higher, 
# which typically represents standard human users rather than system services.
#
# Usage: ./user_list.sh

set -euo pipefail

main() {
  echo "=== System Users (UID >= 1000) ==="
  echo "Username   | UID  | Shell"
  echo "---------------------------"
  
  # Parse /etc/passwd using awk
  # Fields are delimited by ":"
  # $1 = Username, $3 = UID, $7 = Default Shell
  # Filter: UID >= 1000 and ignore the 'nobody' user
  awk -F: '$3 >= 1000 && $1 != "nobody" {printf "% -10s | % -4s | %s\n", $1, $3, $7}' /etc/passwd
}

main "$@"