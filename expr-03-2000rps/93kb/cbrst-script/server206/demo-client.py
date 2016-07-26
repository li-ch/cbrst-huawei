#!/usr/local/bin/python
import subprocess, time

for t in range(60):
    command = "~/cbrst/93k/target/release/client"
    with open("time-{num:02d}-93kb.log".format(num=t), "w") as logfile:
        p = subprocess.Popen(["nice", "-n", "-1", command, "--epoch=2000", "10.67.192.192:50001", "10.67.20.192:50001", "10.67.30.192:50001", "10.67.40.192:50001"], stdout=logfile)
        p.wait()
        logfile.flush()
    time.sleep(1)
