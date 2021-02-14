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
def check_root_full():
    """return true if the root partion is full ,false otherwise"""
    return check_disk_full(disk = '/', min_GB = 2 ,min_percent = 10)

def main():
    """there's a pattern of repeating code in our all checks pi script. For each check that we call, we check if it returns true or false.
        When it returns true, we print an error and exit.  If we add a new check, we'll have to repeat this pattern again."""

    """To avoid code repetition, we'll create a list containing the names of the functions that we want to call,
    and then message to print if the function succeeds.
    After that, we'll add a for loop that iterates over the list of checks and messages.
    Then we'll call check, and if the return value is true,
    print the message and exit with an error code of one. After doing that we can delete the old code that we've already replaced"""

    #we wanna let our script show more than one message if more than one check is failing
    """ we add a Boolean variable called "Everything Ok" before the iteration. 
    Changes variable to false if one of the checks finds a problem, 
    and then exit with an error code only after having done all the checks."""

    everything_ok = True

    checks = [(check_reboot,"Pending Reboot"),(check_root_full, "Root Partion Full")]
    for check,msg in checks :
        if check() :
            print(msg)
            everything_ok = False
    if not everything_ok :
        sys.exit(1)

    print("Everything okay")
    sys.exit(0)
main()
