from TC66C import TC66C
import serial,argparse,math,struct,sys
from Cryptodome.Cipher import AES
from collections import namedtuple
from time import sleep,time,localtime,strftime,monotonic

TC66 = TC66C("/dev/ttyACM0")
	
out_name = 'TC66_'+strftime('%Y%m%d%H%M%S',localtime())+'.csv'
	
f = open(out_name,'w')
f.write('Time[S],Volt[V],Current[A],Power[W]\n')
		
start = monotonic()
now = monotonic()-start
try:			
	while True:
		now = monotonic()-start
		pd = TC66.Poll()
		s = '{:5.1f},{:07.4f},{:07.5f},{:07.4f}'.format(
			now,
			pd.Volt, 
			pd.Current,
			pd.Power)
		f.write(s+'\n')
		print(s)
		elapsed = (monotonic()-start) - now
		if elapsed < 1.0:
			sleep(1.0 - elapsed)
except KeyboardInterrupt:
	f.close()
