import pickle
from datetime import *

input_time = datetime.now()

times = {'mc_donalds':[[time(7,0),time(0,0)],[time(7,0),time(0,0)],[time(10,0),time(22,0)]],
'kfc_':[[time(7,30),time(22,0)],[time(11,0),time(20,0)],[time(11,0),time(20,0)]],
'subway':[[time(8,0),time(21,0)],[time(11,0),time(18,0)],[time(11,0),time(18,0)]],
'pizza_hut':[[time(11,0),time(22,0)],[time(11,0),time(21,0)],[time(11,0),time(20,0)]],
'sandwich_guys':[[time(10,0),time(20,0)],[time(10,0),time(15,0)],None]}

filename = 'times'
outfile = open(filename,'w+b')

pickle.dump(times, outfile)
outfile.close()

# tuple -> (hr, min)
# [mon-fri, sat, sun]
