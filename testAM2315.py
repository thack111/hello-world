import time
from tentacle_pi.AM2315 import AM2315
am = AM2315(0x5c,"/dev/i2c-1")

for x in range(0,10):
    temperature_c, humidity, crc_check = am.sense()
    temperature_f = (temperature_c * 9 / 5) + 32
    print "temperature C: %0.1f" % temperature_c
    print "temperature F: %0.1f" % temperature_f
    print "humidity: %0.1f" % humidity
    print "crc: %s" % crc_check
    print
    time.sleep(2.0)
