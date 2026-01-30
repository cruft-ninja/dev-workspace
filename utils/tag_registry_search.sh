#!/bin/bash
#
# THIS SCRIPT IS DEPRECATED.
# Please use the new unified search script: ./utils/search.sh -t
#

echo "WARNING: This script is deprecated. Please use './utils/search.sh -t <tag>'" >&2
echo ""

# Forward arguments to the new script
exec ./utils/search.sh -t "$@"