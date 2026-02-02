#!/bin/bash
# kill_process.sh: Provides a safe way to terminate processes by name.
#
# This script searches for processes matching a string, displays them, 
# and asks for explicit user confirmation before sending a kill signal.
#
# Usage: ./kill_process.sh <process_name>

set -euo pipefail

usage() {
  echo "Usage: $0 <process_name>"
  exit 1
}

main() {
  # Ensure a process name search term is provided
  if [[ $# -ne 1 ]]; then
    usage
  fi

  local proc_name="$1"
  local pids
  
  # Find PIDs matching the search term
  # 'pgrep -f' matches against the full command line
  # || true ensures the script doesn't exit if no matches are found
  pids=$(pgrep -f "${proc_name}" || true)

  if [[ -z "${pids}" ]]; then
    echo "No processes found matching '${proc_name}'."
    exit 0
  fi

  # Show details of the processes that would be killed
  echo "Found the following processes for '${proc_name}':"
  ps -fp ${pids}
  echo ""
  
  # Request user confirmation
  read -r -p "Are you sure you want to kill these processes? [y/N] " response
  if [[ "${response}" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "Sending termination signal..."
    # Send SIGTERM to the identified PIDs
    kill ${pids}
    echo "Signal sent successfully."
  else
    echo "Operation cancelled by user."
  fi
}

main "$@"