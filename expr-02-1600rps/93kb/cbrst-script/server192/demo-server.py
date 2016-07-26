#!/usr/local/bin/python
import os

os.system("nice -n -1 ~/cbrst/target/release/server 10.67.192.192:50001 10.67.20.192:50001 10.67.30.192:50001 10.67.40.192:50001 &")
