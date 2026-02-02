#!/bin/bash
# find_old.sh: Locates files modified more than a certain number of days ago.
#
# This utility helps in identifying old logs, temporary files, or archives 
# that may be candidates for deletion or compression to save space.
#
# Usage: ./find_old.sh <directory> <days>

set -euo pipefail

# Print usage instructions and exit
usage() {
  echo "Usage: $0 <directory> <days>"
  exit 1
}

main() {
  # Ensure exactly two arguments are provided
  if [[ $# -ne 2 ]]; then
    usage
  fi

  local target_dir="$1"
  local days="$2"

  # Verify the target directory exists
  if [[ ! -d "${target_dir}" ]]; then
    echo "Error: Directory '${target_dir}' does not exist." >&2
    exit 1
  fi

  # Validate that the 'days' argument is a positive integer
  if ! [[ "${days}" =~ ^[0-9]+$ ]]; then
    echo "Error: Days must be a positive integer." >&2
    exit 1
  fi

  echo "Scanning '${target_dir}' for files older than ${days} days..."
  
  # Use the 'find' command with '-mtime' to locate files based on modification time
  # +n matches files modified more than n*24 hours ago
  find "${target_dir}" -type f -mtime +"${days}" -print
}

main "$@"