





import csv
import re
from compute_location_from_gps import compute_location_from_gps
import os

# define boundary
for line in open('../../Preprocessing/Results/boundary'):
  boundary = map(float, line.strip().split(','))

# define minimu distance
#gps_delta = 0.0001  # 10m
gps_delta = 0.001  # 100m

def map_GPS_to_location(filename):
  fout_v = open('../../Preprocessing/Results/data_v','w')
  fout_e = open('../../Preprocessing/Results/data_e','w')
  locationinformation = {}
  fout = open('../../Preprocessing/Results/%s_location' % filename, 'w')
  lineind = -1
  for line in open('../../Data/%s.csv' % filename):
    lineind += 1
    if lineind == 0:
      continue
    words = line.strip().split(',"[')
    if words[1] == ']"':
      continue
    s = '"['
    (pl,pr) = (-1,-1)
    for context in re.sub(r'^\[|]]"','',words[1]).split('],['):
        (l,r) = map(float,context.split(','))
        (l,r) = compute_location_from_gps(boundary, gps_delta,(l,r))
        if pl==-1:
          (pl, pr) = (l,r)
          continue
        if l==pl and r == pr:
          continue
        loc = '%d %d' % (l, r)
        ploc = '%d %d' % (pl, pr)
        fout_v.write("%s\n" % loc)
        if l>pl+1 or r>pr+1:
          print ploc,loc
        fout_e.write("%s %s\n" % (ploc,loc))
        if s == '"[':
          s += '[%d,%d]' % (l,r)
        else:
          s += ',[%d,%d]' % (l,r)
    s += ']"'
    fout.write(words[0] + ',' + s + '\n')
  fout.close()
  fout_e.close()
  fout_v.close()
  pass

def map_location_to_id(filename):
  os.system('cat ../../Preprocessing/Results/locationinformation| sort |uniq -c | sort -k2,2n -k3,3n -k1,1n > ../../Preprocessing/Results/tmp; mv ../../Preprocessing/Results/tmp ../../Preprocessing/Results/locationinformation')
  pass


def map_GPS_to_graph():
  for filename in ['train','test']:
    map_GPS_to_location(filename)
    map_location_to_id(filename)
  pass




if __name__ == '__main__':
  map_GPS_to_graph()






