#!/usr/bin/env python3

from datetime import datetime, timedelta
import random

__author__ = "itismadness"
__version__ = "1.0.0"

__timezones__ = [
    -12, -11, -10, -9.5, -9, -8, -7, -6, -5, -4, -3.5, -3, -2, -1, 0, 1, 2, 3, 3.5, 4, 4.5, 5,
    5.5, 5.75, 6, 6.5, 7, 8, 8.5, 8.75, 9, 9.5, 10, 10.5, 11, 12, 12.75, 13, 14
]


def main():
    timezone = random.choice(__timezones__)
    now = datetime.utcnow() + timedelta(hours=timezone)
    "2017-10-30T21:57:07+0000"
    z = ("-" if timezone < 0 else "+") + "{0:02d}".format(abs(int(timezone)))
    if str(timezone-int(timezone))[2:] == "5":
        z += "30"
    elif str(timezone-int(timezone))[2:] == "75":
        z += "45"
    else:
        z += "00"
    print(now.strftime("%Y-%m-%dT%H:%M:%S") + z)


if __name__ == "__main__":
    main()
