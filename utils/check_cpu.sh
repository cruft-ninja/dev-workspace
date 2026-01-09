# check_cpu.sh
#!/bin/bash

# 1. Capture a single snapshot of system tasks in batch mode
# 2. Extract the line containing CPU percentages
# 3. Parse the 'idle' percentage and subtract from 100
# 4. Output the result as a percentage

cpu_load=$(top -bn1 | grep "Cpu(s)" | \
           sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \
           awk '{print 100 - $1}')

echo "Current CPU Load: ${cpu_load}%"

# Example logic: Trigger alert if load exceeds 90%
if (( $(echo "$cpu_load > 90.0" | bc -l) )); then
    echo "WARNING: High CPU usage detected!"
fi