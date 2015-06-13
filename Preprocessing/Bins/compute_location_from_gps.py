






def compute_location_from_gps(boundary, gps_delta, gps):
  return (int( (gps[0]-boundary[0])/gps_delta ) ,int( (gps[1]-boundary[2])/gps_delta ))
  pass


if __name__ == '__main__':
  # define boundary
  for line in open('../../Preprocessing/Results/boundary'):
    boundary = map(float, line.strip().split(','))
  # define minimu distance
  #gps_delta = 0.0001  # 10m
  gps_delta = 0.001  # 100m
  gps = (-8.585676,41.148522)
  location = compute_location_from_gps(boundary, gps_delta, gps)
  print location
