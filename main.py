from __future__ import print_function
from builtins import input
import datetime

dat = "%A, %Y %B %d %H:%M"
now = datetime.datetime.now()

print(now.strftime(dat), end="")
input()
