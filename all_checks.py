#!/usr/bin/env python3
import os
import sys
def check_reboot():
    """return true if computer has pending rebot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("pending reboot")
        sys.exit(1)
    print("okay")
    sys.exit(0)
main()
