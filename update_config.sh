#!/bin/bash
if test -e "ssh_config";then
    cp ssh_config ~/.ssh/config
fi
echo 'Run update ssh config script'
