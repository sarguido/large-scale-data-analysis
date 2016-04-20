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

When you are done, run:

```
vagrant destroy
```

