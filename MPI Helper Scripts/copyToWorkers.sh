# Prompt User to list directory
read -p 'List local directory? [Y/N]: ' -n 1 -r
if  [[ $REPLY =~ ^[Yy]$ ]]
then 
        echo ' '
        ls
fi
echo ' '

# Prompt for files
read -p 'File(s): ' files
echo ' '

# Confirm

echo 'File(s) to copy: ' files
echo ' '
read -p 'Is this correct? [Y/N]: ' -n 1 -r

# If info is correct, run the script
if  [[ $REPLY =~ ^[Yy]$ ]]
then 
        # Copy Files
        for node in node1 node2 node3 node4 node5; do
            scp $files $node:/home/mpi/;
        done
fi
echo ' '
echo 'END SCRIPT'
