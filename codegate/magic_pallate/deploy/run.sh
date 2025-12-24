#!/bin/bash

if [ ! -f /home/$user/flag ]; then
    echo $FLAG > /home/$user/flag
    unset FLAG
    chmod 444 /home/$user/flag
fi

su -c "./prob" $user
