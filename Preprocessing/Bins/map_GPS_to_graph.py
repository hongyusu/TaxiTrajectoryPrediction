





import csv
import re
from compute_location_from_gps import compute_location_from_gps

# define boundary
for line in open('../../Preprocessing/Results/boundary'):
  boundary = map(float, line.strip().split(','))

# define minimu distance
#gps_delta = 0.0001  # 10m
gps_delta = 0.001  # 100m

def map_GPS_to_location(filename):
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
        if l==pl and r == pr:
          continue
        if not l in locationinformation.keys():
          locationinformation[l] = {}
        if not r in locationinformation[l].keys():
          locationinformation[l][r] = 0
        locationinformation[l][r] += 1
        (pl, pr) = (l,r)
        if s == '"[':
          s += '[%d,%d]' % (l,r)
        else:
          s += ',[%d,%d]' % (l,r)
    s += ']"'
    fout.write(words[0] + ',' + s + '\n')
  fout.close()
  fout = open('../../Preprocessing/Results/locationsinformation','w')
  for l in locationinformation.keys():
    for r in locationinformation[l].keys():
      fout.write('%d %d %d\n' % (l,r,locationinformation[l][r]))
  fout.close()
  pass

def map_location_to_id(filename):
  pass


def map_GPS_to_graph():
  for filename in ['train','test']:
    map_GPS_to_location(filename)
    map_location_to_id(filename)
  pass




if __name__ == '__main__':
  map_GPS_to_graph()






