#!/bin/bash

BASEDIR=/Users/Keshav/Documents/Code/Project/
IMGCAP=$BASEDIR/ImageSnap-v0.2.5/

open_prompt ()
{
    echo -n "Would you like to play a game? [Y/n] "
    read playGame
}

commence_game ()
{

    tput clear
    cat <<"EOT"
      .___.
     /     \
    | O _ O |
    /  \_/  \ 
  .' /     \ `.
 / _|       |_ \
(_/ |       | \_)
    \       /
   __\_>-<_/__
   ~;/     \;~
===================
     WELCOME
===================

EOT

    sleep 2
    
    $BASEDIR/img_cap.sh

}

open_prompt
while [[ -z "$playGame" ||  ("$playGame" != "Y" && "$playGame" != "n") ]]
do
    echo "Must input either Y or n. Returning back to prompt..."
    sleep 2
    tput clear
    open_prompt
    echo $playGame
done

if [[ "$playGame" == "n" ]]
then
    echo "Good answer."
    exit 1

else
    commence_game
fi
