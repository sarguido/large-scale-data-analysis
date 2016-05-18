# VM Stuffs

Trying to get everybody to install hadoop and spark on thier environment as part of the tutorial is a path to dispare and madness.  Accordingly, we're going to provide everybody with a VM with everything pre-installed to minimize the install-fest portion of the day.

We're using vagrant to manage the VM as it's free and can run on most sane platforms.

## Getting started

Before you can do anything you will need to install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).  Technically, you can use other VMs than virtual box but if you want to go down that path, you are on your own.

## Using the VM

To start a VM cd into this directory and run:

```
vagrant up
```

All files in this directory will be available and synced to the vm in the `/vagrant` directory.  Makes it easy to edit files locally but then run them on the vm.

To ssh into the vm, run:

```
vagrant ssh
```

When you are done, run:

```
vagrant destroy
```



## Web UI Links

[Hadoop UI](http://my-hadoops:8088/cluster)
[Spark UI](http://my-hadoops:18080/)


## Plan B - https://blog.cloudera.com/blog/2014/06/how-to-install-a-virtual-apache-hadoop-cluster-with-vagrant-and-cloudera-manager/