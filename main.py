import arpfinder
if arpfinder.CheckArp('192.168.1.1')==0:
    print 'This is normal status'
else:
    print 'Warning! Attack was started!'