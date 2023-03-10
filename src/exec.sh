# Exec.sh by Daniel Tellez
# Purpose:  
#		Accepts a given filepath, <filepath> as argument
#		and executes main.py on that source code file.
#		Output is written to STDOUT

#!/bin/bash

# Invoke the ./main.py script passing in all arguments
python3 ./main.py $@