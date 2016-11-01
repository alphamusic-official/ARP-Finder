import os
import subprocess
import time
def checkMac(addrs):
    proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    while 1:
        output = proc.stdout.readline()
        if "." in output:
            break

    proc.stdin.write('arp -a\r\n')
    while 1:
        output = proc.stdout.readline()
        if addrs in output:
            break
    proc.kill()
    time.sleep(5)
    return output[24:41]
def CheckArp(addrs):
    mac_ars = checkMac(addrs)
    if mac_ars!=checkMac(addrs):
        return 1
    else:
        return 0