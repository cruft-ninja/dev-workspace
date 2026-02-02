#!/bin/bash
# backup_dir.sh: Creates a timestamped compressed archive of a directory.
#
# This script automates the process of backing up a folder into a .tar.gz file.
# It ensures the destination exists and handles path resolution for the archive.
#
# Usage: ./backup_dir.sh <source_dir> <backup_dest>

set -euo pipefail

usage() {
  echo "Usage: $0 <source_dir> <backup_dest>"
  exit 1
}

main() {
  # Check for correct number of arguments
  if [[ $# -ne 2 ]]; then
    usage
  fi

  local src="$1"
  local dest="$2"
  
  # Create a timestamp string (e.g., 20231027_143005)
  local timestamp
  timestamp=$(date +%Y%m%d_%H%M%S)
  
  # Extract the directory name and construct the archive filename
  local archive_name
  archive_name="$(basename "${src}")_${timestamp}.tar.gz"
  local archive_path="${dest}/${archive_name}"

  # Check if the source directory actually exists
  if [[ ! -d "${src}" ]]; then
    echo "Error: Source directory '${src}' does not exist." >&2
    exit 1
  fi

  # Create the destination directory if it doesn't already exist
  if [[ ! -d "${dest}" ]]; then
    echo "Creating destination directory '${dest}'..."
    mkdir -p "${dest}"
  fi

  echo "Backing up '${src}' to '${archive_path}'..."
  
  # Create the compressed tar archive
  # -c: Create, -z: Gzip compression, -f: Filename
  # -C: Change to the parent directory of source to avoid nested paths in the archive
  tar -czf "${archive_path}" -C "$(dirname "${src}")" "$(basename "${src}")"
  
  echo "Backup complete: ${archive_name}"
}

main "$@"