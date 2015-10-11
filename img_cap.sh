#!/bin/bash

BASEDIR="/Users/Keshav/Documents/Code/WhIP\ 2.0\ -\ Source\ Code/"
TIME_MONITOR=11
TIME_INTERVAL=1

ASLEEP=true
VERBOSE=false
COUNTER=5

# display usage
display_usage()
{
    echo "$(basename $0) [-t|--totaltime T] [-i|--interval I] [-v|--verbose]"
    echo "  T   = total time monitoring (default 3 seconds)"
    echo "  I   = interval between camera activation (default 11 second)"
}

# the image capturing
img_cap ()
{
    if $VERBOSE; then echo "Commence monitoring...Taking pictures every $TIME_INTERVAL seconds for $TIME_MONITOR seconds"; fi
    TIME="1"
    NUM_SLEEP=0

    while [[ $TIME -lt $TIME_MONITOR ]]
    do
	if [[ $(($TIME % $TIME_INTERVAL)) -eq 0 ]]
	then
            #osascript $BASEDIR/screen_brighter.scpt
	    if $VERBOSE; then REMAINDER=$(echo "$TIME_MONITOR-$TIME" | bc); echo "Been monitoring for $TIME seconds. Total monitor time remaining: $REMAINDER seconds"; fi
	    NEXT_PICTURE="snapshot.jpg"
	    imagesnap -w 2 $NEXT_PICTURE &> /dev/null
	    # filler method for detecting eyes
	    RESPONSE=$(python temp/stuff.py 2>&1)
	    echo $RESPONSE
	    if [[ $RESPONSE == "closed" ]]
	    then
		let "NUM_SLEEP++"
		echo "bad"
	    fi

	    if [[ $NUM_SLEEP -eq $COUNTER ]]
	    then 
		mv $NEXT_PICTURE asleep.jpg
		python asleep.py
		exit 1
	    fi
	fi
	sleep 1
	let "TIME++"
    done
}

# temporary clean-up command
clean_up()
{
    rm $BASEDIR/snapshot-*jpg

}


# method call

while [[ $# > 0 ]] 
do
    key=$1
    case $key in
        -t|--totaltime)
	    TIME_MONITOR=$2
            shift
            ;;
        -i|--interval)
	    TIME_INTERVAL=$2
            shift
            ;;
        -v|--verbose)
	    VERBOSE=true
            ;;
	-h|--help)
	    display_usage
	    exit 1
    esac
    shift
done

img_cap
#clean_up