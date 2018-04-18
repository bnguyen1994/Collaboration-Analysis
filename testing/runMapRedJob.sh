#/bin/bash
#/home/hadoop

# Script to prompt the user for the mapred files and input and output files

# Splash Screen
cat splashScreen.txt

# Prompt User
read -p 'Mapper Program (py): ' mapperFile
read -p 'Reducer Program (py): ' reducerFile
read -p 'Input File (HDFS dir): ' inputFile
read -p 'Output File (HDFS dir): ' outputFile

# Confirm
echo ' '
echo Mapper Program: $mapperFile
echo Reducer Program: $reducerFile
echo Input File: hdfs://$inputFile
echo Output File: hdfs://$outputFile
echo ' '
read -p 'Is this correct? [Y/N]: ' -n 1 -r

# If info is correct, run the script
if  [[ $REPLY =~ ^[Yy]$ ]]
then 
	echo ' '
	hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.0.jar -files $mapperFile,$reducerFile -mapper $mapperFile -reducer $reducerFile -input hdfs://$inputFile -output $outputFile

	# Prompt to grab file from HDFS
	echo ' '
	read -p 'Get the file from HDFS? [Y/N]: ' -n 1 -r
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		echo ' '
		hdfs dfs -get $outputFile
	fi
fi
echo ' '
exit 1

