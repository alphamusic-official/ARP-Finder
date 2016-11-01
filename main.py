import arpfinder
mac_ars = arpfinder.checkMac(addrs)
if arpfinder.CheckArp('192.168.1.1',mac_addrs)==0:
    print 'This is normal status'
else:
    print 'Warning! Attack was started!'