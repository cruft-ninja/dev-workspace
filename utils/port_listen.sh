#!/bin/bash
# port_listen.sh: Identifies all network services currently listening for connections.
#
# This script uses the 'ss' utility (socket statistics) to list active 
# TCP and UDP listeners, showing the associated port and process.
#
# Usage: ./port_listen.sh

set -euo pipefail

main() {
  # Verify that the 'ss' command is available on the system
  if ! command -v ss &> /dev/null; then
    echo "Error: 'ss' command not found. Please install the iproute2 package." >&2
    exit 1
  fi

  echo "=== Active Listening Ports ==="
  # Flags:
  # -t: Display TCP sockets
  # -u: Display UDP sockets
  # -l: Display only listening sockets
  # -n: Show numeric port numbers (don't resolve service names)
  # -p: Show the process using the socket (requires sufficient permissions)
  ss -tulnp
}

main "$@"