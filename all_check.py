#!/usr/bin/env python

import os
import sys
import shutil
import socket

#New check for reboot
def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

#New check if disk over limit
def check_disk_full(disk, min_gb, min_percent):
    """Return True if there isn't enought disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    #Calculate the precentage of the free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_gb or gigabytes_free < min_gb:
        return True
    return False

#New check if root full
def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

#New check for network
def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

#Main function starts here
def main():
    checks=[
        (check_reboot, "Pending Reboot! Ddue"),
        (check_root_full, "Root partition full! Dude"),
        (check_no_network, "No working netowrk"),
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok! Dude.")
    sys.exit(0)

main()
