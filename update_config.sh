#!/bin/bash
if test -e "ssh_config";then
    cp ssh_config ~/.ssh/config
fi
if test -e "sysHostFilePart";then
    if test -e "/home/tutorial/hosts.bak";then
        cp ~/hosts.bak /etc/hosts
        cat sysHostFilePart >> /etc/hosts
    fi
fi
echo 'Run update ssh config script'

