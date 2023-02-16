# Exec.sh by Daniel Tellez
# Purpose:  
#		Accepts a given filepath, <filepath> as argument
#		and executes compliler on that source code file.
#		Output is written to STDOUT

#!/bin/bash

# Check for only one exact command-line argument
if [ "$#" -ne 1 ]; then
    printf 'ERROR! Please input a valid input file\n' >&2
    exit 1
fi

# Invoke the ./main.py script
python3 ./main.py $1