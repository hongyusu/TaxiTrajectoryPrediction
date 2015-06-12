
# Taxi Trajectory Prediction, ECML-PKDD 2015

## Data preprocessing

1. Find the boundary of all the trajectories in terms of a square region.
   1. This is achieved by the python scripts `Preprocessing/Bins/find_boundary.py`.
   1. The result is in the file `Preprocessing/Results/boundary`.
   1. The square region is defined by

      	-8.729766,-7.542072,41.062563,41.562351