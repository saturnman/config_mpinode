#!/bin/bash
while [ true ]
do 
    if test -e "ssh_config";then
        cp ssh_config ~/.ssh/config
    fi
    echo 'Hello from mpi node'
    sleep 10;
done
