#!/bin/bash

j=0
for file in $(ls -al "$1") ;  do
	((j=j+1))
	if [[ "$j" -eq 5 ]] ;  then	       	
		if [[ "$file" -eq 0 ]] ; then  
			echo "$1 --> $file octet(s)"
		fi
	fi 
done
