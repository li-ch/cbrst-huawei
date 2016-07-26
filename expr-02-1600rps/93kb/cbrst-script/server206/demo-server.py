#!/usr/local/bin/python
import os

os.system("nice -n -1 ~/cbrst/target/release/server 10.67.192.206:50001 10.67.20.206:50001 10.67.30.206:50001 10.67.40.206:50001 &")
