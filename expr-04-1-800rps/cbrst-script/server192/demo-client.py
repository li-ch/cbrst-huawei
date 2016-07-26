#!/usr/local/bin/python
import subprocess, time, random

num_iter = 10
num_msg = 800

for t in range(num_iter):
    command = [
        ["/home/lich/cbrst/5k/target/release/client", "--epoch={}".format(num_msg), "192.168.10.206:50001", "192.168.20.206:50001", "192.168.30.206:50001", "192.168.40.206:50001"], 
        ["/home/lich/cbrst/20k/target/release/client", "--epoch={}".format(num_msg), "192.168.10.206:50002", "192.168.20.206:50002", "192.168.30.206:50002", "192.168.40.206:50002"], 
        ["/home/lich/cbrst/93k/target/release/client", "--epoch={}".format(num_msg), "192.168.10.206:50003", "192.168.20.206:50003", "192.168.30.206:50003", "192.168.40.206:50003"]
        ]
    with open("time-{num:02d}-all.log".format(num=t), "w") as logfile:
        p = subprocess.Popen(random.choice(command), stdout=logfile)
        p.wait()
        logfile.flush()
    time.sleep(1)

# combine into one file
# with open("all", 'w') as outfile:
#     for t in range(num_iter):
#         with open("time-{num:02d}-all.log".format(num=t), 'r') as readfile:
#             outfile.write(readfile.read())
