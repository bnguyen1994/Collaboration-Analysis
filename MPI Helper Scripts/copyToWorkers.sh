# Prompt User to list directory

# Check for commandline arguement
if [ -z "$1" ]
then
        echo 'ERROR: No commandline arguements'
        echo ' '
        echo 'SYNTAX: "./copyToWorkers.sh <file>"'
        echo ' '
        echo 'END SCRIPT'
        exit 0
fi

# Confirm
echo 'File(s) to copy: ' $1
echo ' '
read -p 'Is this correct? [Y/N]: ' -n 1 -r

# If info is correct, run the script
if  [[ $REPLY =~ ^[Yy]$ ]]
then 
        # Copy Files
        for node in node1 node2 node3 node4 node5; do
            scp $1 $node:/home/mpi/;
        done
fi
echo ' '
echo 'END SCRIPT'
exit 1
