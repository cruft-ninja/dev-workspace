#!/bin/bash
# sys_info.sh: Displays a high-level overview of system status.
#
# This script aggregates several basic system metrics (kernel version, uptime, 
# memory, and root disk usage) into a single, easy-to-read report.
#
# Usage: ./sys_info.sh

set -euo pipefail

main() {
  echo "=== System Health Summary ==="
  echo "Report Generated: $(date)"
  echo "Kernel Version:   $(uname -r)"
  echo "System Uptime:    $(uptime -p)"
  echo ""
  
  # Memory Usage Summary
  # Uses 'free' to get stats and 'awk' to calculate percentage
  echo "--- Memory Resource Status ---"
  free -h | awk 'NR==2{printf "Used: %s / Total: %s (Usage: %.2f%%)\n", $3, $2, $3/$2*100}'
  echo ""
  
  # Disk Usage Summary (Root Filesystem)
  # Uses 'df' to get stats for the root partition
  echo "--- Disk Space Status (/) ---"
  df -h / | awk 'NR==2{printf "Used: %s / Total: %s (Available: %s)\n", $3, $2, $4}'
}

main "$@"