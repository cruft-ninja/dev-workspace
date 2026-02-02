#!/bin/bash
# disk_monitor.sh: Proactively monitors disk usage on the root filesystem.
#
# This script checks the percentage of disk space used on the '/' partition.
# If the usage exceeds a defined threshold, it prints a warning.
# This is useful for automated health checks and cron jobs.
#
# Usage: ./disk_monitor.sh [threshold_percentage] (default 90)

set -euo pipefail

main() {
  # Set threshold from argument or default to 90%
  local threshold="${1:-90}"

  # Validate that the threshold is a numeric integer
  if ! [[ "${threshold}" =~ ^[0-9]+$ ]]; then
    echo "Error: Threshold must be an integer." >&2
    exit 1
  fi

  echo "Checking disk usage (Threshold: ${threshold}%)..."
  
  # Parse df output for root filesystem /
  # --output=pcent specifically requests the percentage used field
  # awk extracts the numeric value from the second line
  # tr removes the '%' character for integer comparison
  local usage
  usage=$(df / --output=pcent | awk 'NR==2 {print $1}' | tr -d '%')

  # Compare current usage against the threshold
  if [[ "${usage}" -ge "${threshold}" ]]; then
    echo "WARNING: Disk usage is high: ${usage}%"
    exit 1
  else
    echo "OK: Disk usage is normal: ${usage}%"
  fi
}

# Execute main function with all script arguments
main "$@"