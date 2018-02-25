#!/usr/bin/env python
#
# coa.py
# Imports and builds the environment for the book:
#
# Preparing for the Certified Openstack Administator Exam
# https://www.packtpub.com/virtualization-and-cloud/preparing-certified-openstack-administrator-exam
#
# TO DO:
# * Error handling. more of it
# * Environment removal

import apt
import sys
import subprocess
import os


def virtualbox():
    '''
    Checks virtualbox is installed and installs it
    '''

    pkg_name = "virtualbox"
    cache = apt.cache.Cache()
    cache.open(None)
    pkg = cache[pkg_name]
    if pkg.is_installed:
        installed = (
            'Hey! Check that out -> {pkg_name} is already installed '
            ':-)').format(pkg_name=pkg_name)
        print(installed)
    else:
        try:
            print "Installing {pkg_name}...".format(pkg_name=pkg_name)
            # Could not find a python "sudo" module
            subprocess.Popen(['/usr/bin/sudo', '-S', 'apt-get', 'install', '-y', pkg_name])
        except Exception, arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))


def coaAppliance():
    '''
    Downloads the COA appliance
    Imports it into Virtualbox
    '''
    downloading = (
        'Downloading the ova from '
        'Preparing-for-the-Certified-OpenStack-Administrator-Exam...')
    print(downloading)
    local_dir = os.path.expandvars('$HOME')
    user = os.environ["USER"]
    coa_url = (
        'https://github.com/PacktPublishing/Preparing-for-the-Certified-'
        'OpenStack-Administrator-Exam/raw/master')
    coa_ova = "coa-aio-newton.ova"
    print "Downloading the COA appliance"
    dl_cmd = "/usr/bin/wget -P {0} {1}/{2}".format(local_dir, coa_url, coa_ova)
    print dl_cmd
    subprocess.call(dl_cmd, shell=True)
    import_cmd = (
        '/usr/bin/vboxmanage import {0}/{1} --vsys 0 --vmname {2}-coa').format(
            local_dir, coa_ova, user)
    print import_cmd
    subprocess.call(import_cmd, shell=True)


virtualbox()
coaAppliance()
