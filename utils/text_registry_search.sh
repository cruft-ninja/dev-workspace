#!/bin/bash
#
# THIS SCRIPT IS DEPRECATED.
# Please use the new unified search script: ./utils/search.sh
#

echo "WARNING: This script is deprecated. Please use './utils/search.sh <term>'" >&2
echo ""

# Forward arguments to the new script
exec ./utils/search.sh "$@"