#!/usr/bin/env python

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Return True if there isn't enought disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    #Calculate the precentage of the free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

#Just adding comment for some testing
def main():
    if check_reboot():
        print("Pending Reboot! Dude.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10)
        print("Disk full! Dude.")
        sys.exit(1)

    print("Everything ok! Dude.")
    sys.exit(0)

main()