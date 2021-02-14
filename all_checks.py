#!/usr/bin/env python3
import os
import sys
import shutil

def check_reboot():
    """return true if computer has pending rebot."""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk,min_GB,min_percent):
    """return true if there's not free disk space ,false otherwise"""
    du = shutil.disk_usage(disk)
    #calculate percentage of free space
    percent_free = 100 * du.free /du.total
    #calculate how many free gigabites
    gigabites_free = du.free / 2**30
    if percent_free < min_percent or gigabites_free < min_GB :
        return True
    return False
def check_full():
    """return true if the root partion is full ,false otherwise"""
    return check_disk_full(disk = '/', min_GB = 2 ,min_percent = 10)

def main():
    """there's a pattern of repeating code in our all checks pi script. For each check that we call, we check if it returns true or false.
        When it returns true, we print an error and exit.  If we add a new check, we'll have to repeat this pattern again."""
    if check_reboot():
        print("pending reboot")
        sys.exit(1)

    if check_full():
        print("root partion Full.")
        sys.exit(1)

    print("Everything okay")
    sys.exit(0)
main()
