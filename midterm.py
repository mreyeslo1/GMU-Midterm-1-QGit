#!/usr/bin/env python


import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

# Get the current feed-forward (state) 
[statuss, framesizes] = s.get(state, wait=False, last=False)

#move hips and ankles to shift center of mass to left side 
for i in range(0,5):
	
	ref.ref[ha.LHR] = 0 + (0.04*i)
	ref.ref[ha.RHR] = 0 + (0.04*i)
	ref.ref[ha.LAR] = 0 - (0.04*i)
	ref.ref[ha.RAR] = 0 - (0.04*i)
	r.put(ref)
	time.sleep(2)

time.sleep(3)

#lift the left leg up
for i in range(0,5):
	ref.ref[ha.LHP] = 0 - (0.2*i)
	ref.ref[ha.LKN] = 0 + (0.4*i)
	ref.ref[ha.LAP] = 0 - (0.2*i)

	r.put(ref)
	time.sleep(2)

time.sleep(3)

for j in range(0,2):
	for i in range(0,7):
		ref.ref[ha.RHP] = -0 - (0.1*i)
		ref.ref[ha.RKN] = 0 + (0.2*i)
		ref.ref[ha.RAP] = -0 - (0.1*i)
		r.put(ref)
		time.sleep(1.5)

	for i in range(0,7):
	
		ref.ref[ha.RHP] = -0.7 + (0.1*i)
		ref.ref[ha.RKN] = 1.4 - (0.2*i)
		ref.ref[ha.RAP] = -0.7 + (0.1*i)
		r.put(ref)
		time.sleep(1.5)


#lift the right leg up
for i in range(0,5):
	ref.ref[ha.LHP] =  -1 + (0.2*i)
	ref.ref[ha.LKN] = 2 - (0.4*i)
	ref.ref[ha.LAP] =  -1 + (0.2*i)

	r.put(ref)
	time.sleep(2)

time.sleep(3)


for i in range(0,5):
	
	ref.ref[ha.LHR] = .2 - (0.04*i)
	ref.ref[ha.RHR] = .2 - (0.04*i)
	ref.ref[ha.LAR] = -.2 + (0.04*i)
	ref.ref[ha.RAR] = -.2 + (0.04*i)
	r.put(ref)
	time.sleep(4)

time.sleep(10)
#####
ref.ref[ha.RHR] = 0 
ref.ref[ha.LHR] = 0 
ref.ref[ha.RAR] = 0
ref.ref[ha.LAR] = 0
ref.ref[ha.RHP] = 0 
ref.ref[ha.RKN] = 0 
ref.ref[ha.RAP] = 0 
r.put(ref)

time.sleep(10)


#####

for i in range(0,5):
	
	ref.ref[ha.RHR] = 0 - (0.04*i)
	ref.ref[ha.LHR] = 0 - (0.04*i)
	ref.ref[ha.RAR] = 0 + (0.04*i)
	ref.ref[ha.LAR] = 0 + (0.04*i)
	r.put(ref)
	time.sleep(2)

time.sleep(10)

#lift the right leg up
for i in range(0,5):
	ref.ref[ha.RHP] = -0 - (0.2*i)
	ref.ref[ha.RKN] = 0 + (0.4*i)
	ref.ref[ha.RAP] = -0 - (0.2*i)

	r.put(ref)
	time.sleep(3)

time.sleep(10)

for j in range(0,2):
	for i in range(0,4):
		ref.ref[ha.LHP] = -0 - (0.1*i)
		ref.ref[ha.LKN] = 0 + (0.2*i)
		ref.ref[ha.LAP] = -0 - (0.1*i)
		r.put(ref)
		time.sleep(1.5)

	for i in range(0,4):
	
		ref.ref[ha.LHP] = -0.4 + (0.1*i)
		ref.ref[ha.LKN] = 0.8 - (0.2*i)
		ref.ref[ha.LAP] = -0.4 + (0.1*i)
		r.put(ref)
		time.sleep(1.5)


r.close()
s.close()





