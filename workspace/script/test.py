#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Docurdt Wang'

import os
import socket

##work flow
##network setup
##hosts
##adduser
    #sudo newusers < user
    #sudo chpasswd < passwd

#####on master ###sudo apt-get install nfs-kernel-server

###on all nodes### sudo apt-get install nfs-common
# install ssh
#install putty-tools

###master nodes file changes###  /etc/exports
    ##/home/mpiuser *(rw,sync,no_subtree_check)

#master node# sudo exportfs -a

#master node set firewall# sudo ufw allow from 192.168.1.0/24

#node1:~$ sudo mount master:/home/mpiuser /home/mpiuser
#compute node# /etc/fstab #master:/home/mpiuser /home/mpiuser nfs

## ssh configure ssh-keygen    ssh-copy-id localhost

## all nodes## sudo apt-get install mpich2

# on master node # touch hosts

#using hydry # mpiuser@master:~$ mpiexec -f hosts -n 3 /home/mpiuser/bin/cpi

#install torque
    #[root]# apt-get update
    #[root]# apt-get install libxml2-devel openssl-devel gcc gcc-c++
    #       [root]# tar -xzvf torque-4.2.9.tar.gz
    #[root]# cd torque-4.2.9/
    #./configure
    #[root]# make
    #[root]# make install
    #make packages
    #> cp torque-package-mom-linux-i686.sh /shared/storage/
    #> cp torque-package-clients-linux-i686.sh /shared/storage/

    ##for i in node01 node02 node03 node04 ; do ssh ${i} /tmp/torque-package-mom-linux-i686.sh --install ; done
    ##for i in node01 node02 node03 node04 ; do ssh ${i} /tmp/torque-package-clients-linux-i686.sh --install ; done

    #cp contrib/init.d/debian.pbs_mom /etc/init.d/pbs_mom
    #update-rc.d pbs_mom defaults
    #cp contrib/init.d/debian.pbs_server /etc/init.d/pbs_server
    #pdate-rc.d pbs_server defaults


    #The following example shows a possible node file listing.
    #TORQUE_HOME/server_priv/nodes:
    ## Nodes 001 and 003-005 are cluster nodes
    ##
    #node001 np=2 cluster01 rackNumber22
    ##
    ## node002 will be replaced soon
    #node002:ts waitingToBeReplaced
    ## node002 will be replaced soon
    ##
    #   node003 np=4 cluster01 rackNumber24
    #node004 cluster01 rackNumber25
    #node005 np=2 cluster01 rackNumber26 RAM16GB
    #node006
    #node007 np=2
    #node008:ts np=4

#install maui
    #tar -xzvf maui-3.3.1.tar.gz
    #cd maui-3.3.1/
    #./configure
    #make
    #make install
        #cp contrib/init.d/maui /etc/init.d/maui
        #pdate-rc.d maui defaults

#install matlab
    #mount iso
    #copy the configure files
    #install


#os.system("mkdir xxx")
def hostconfig():
    try:
        f = open('/etc/hosts', 'a')
        f.write('172.16.0.5 master\n')
        f.write('172.16.0.2 node1\n')
        f.write('172.16.0.3 node2\n')
        f.write('172.16.0.4 node3\n')
        f.write('172.16.0.6 node4\n')
        f.write('172.16.0.7 node5\n')
        f.write('172.16.0.8 node6\n')
    finally:
        f.close()

def netconfig():
    curHost = socket.gethostname()
    #print curHost
    try:
        f = open('/etc/network/interfaces', 'a')
        f.write('auto eth0\n')
        f.write('iface eth0 inet static\n')
        if curHost == 'node1':
            f.write('address 172.16.0.2\n')
        elif curHost == 'node2':
            f.write('address 172.16.0.3\n')
        elif curHost == 'node3':
            f.write('address 172.16.0.4\n')
        elif curHost == 'node4':
            f.write('address 172.16.0.6\n')
        elif curHost == 'node5':
            f.write('address 172.16.0.7\n')
        elif curHost == 'node6':
            f.write('address 172.16.0.8\n')
        else:
            pass
        f.write('netmask 255.255.255.0\n')
    finally:
        f.close()
    os.system('sudo /etc/init.d/networking restart')








if __name__=='__main__':
    #hostconfig()
    #netconfig()
