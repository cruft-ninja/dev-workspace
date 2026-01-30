#!/bin/bash
#
# Description: A versatile search script to find text or tags in a directory.
# Usage: ./search.sh [-d <directory>] [-t] <search_term>

set -euo pipefail

# Default search directory
DEFAULT_DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/registry/docs"

usage() {
  echo "Usage: $0 [-d <directory>] [-t] <search_term>"
  echo "  -d <directory>  Specify a directory to search in (default: $DEFAULT_DOCS_DIR)"
  echo "  -t              Search only within 'tags:' lines"
  echo "  <search_term>   Regex pattern to search for"
  exit 1
}

main() {
  local search_dir="$DEFAULT_DOCS_DIR"
  local search_tags=false
  local term=""

  while getopts ":d:t" opt; do
    case ${opt} in
      d) search_dir="$OPTARG" ;;
      t) search_tags=true ;;
      \?) echo "Invalid option: -$OPTARG" >&2; usage ;;
    esac
  done
  shift $((OPTIND -1))

  term="${1:-}"

  if [[ -z "$term" ]]; then
    echo "Error: Search term required." >&2
    usage
  fi

  if [[ ! -d "$search_dir" ]]; then
    echo "Error: Directory '$search_dir' does not exist." >&2
    exit 1
  fi

  echo "Searching in: $search_dir"

  if [[ "$search_tags" == true ]]; then
    echo "Mode: Tag Search ($term)"
    grep -irl "^tags:.*$term" "$search_dir" || true
  else
    echo "Mode: Full Text Search ($term)"
    grep -ril "$term" "$search_dir" || true
  fi
}

main "$@"
