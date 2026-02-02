#!/bin/bash
# check_site.sh: Verifies if a website is responsive via HTTP/HTTPS.
#
# This script uses 'curl' to perform a HEAD-like request (fetching status code only)
# to check if a remote server is reachable and serving a valid response.
#
# Usage: ./check_site.sh <url>

set -euo pipefail

usage() {
  echo "Usage: $0 <url>"
  exit 1
}

main() {
  # Ensure a URL argument is provided
  if [[ $# -ne 1 ]]; then
    usage
  fi

  local url="$1"
  local status_code

  echo "Checking accessibility of: ${url}..."
  
  # Use curl to fetch only the HTTP status code
  # -o /dev/null: Discard the response body
  # -s: Silent mode
  # -w: Format the output to show only the http_code
  status_code=$(curl -o /dev/null -s -w "%{http_code}\n" "${url}")

  # Check if the status code is in the success/redirection range (200-399)
  if [[ "${status_code}" -ge 200 && "${status_code}" -lt 400 ]]; then
    echo "OK: ${url} is reachable (Status: ${status_code})."
  else
    echo "FAIL: ${url} returned an error or is unreachable (Status: ${status_code})."
    exit 1
  fi
}

main "$@"