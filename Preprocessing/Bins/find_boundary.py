

import csv
import numpy as np
import re


def find_boundary():
  boundary = [0,0,0,0]
  for filename in ['train','test']:
    with open('../../Data/%s.csv' % filename) as fin:
      data = csv.reader(fin)
      lineind = -1
      for line in data:
        lineind += 1
        if lineind == 0:
          continue
        if line[8] == '[]':
          continue
        for words in re.sub(r"\[\[|]]",'',line[8]).split('],['):
          (l,r) = map(float,words.split(','))
          if lineind == 1:
            boundary = [l,l,r,r]
          else:
            if boundary[0] > l:
              boundary[0] = l
            if boundary[1] < l:
              boundary[1] = l
            if boundary[2] > r:
              boundary[2] = r
            if boundary[3] < r:
              boundary[3] = r
  fout = open('../../Preprocessing/Results/boundary','w')
  fout.write('%s\n' % ','.join(map(str,boundary)))
  fout.close()
  pass



if __name__ == '__main__':
  find_boundary()
