#!/usr/local/bin/python
import os

os.system("nice -n -1 /home/lich/cbrst/5k/target/release/server 192.168.10.192:50001 192.168.20.192:50001 192.168.30.192:50001 192.168.40.192:50001 &")
os.system("nice -n -1 /home/lich/cbrst/20k/target/release/server 192.168.10.192:50002 192.168.20.192:50002 192.168.30.192:50002 192.168.40.192:50002 &")
os.system("nice -n -1 /home/lich/cbrst/30k/target/release/server 192.168.10.192:50003 192.168.20.192:50003 192.168.30.192:50003 192.168.40.192:50003 &")
