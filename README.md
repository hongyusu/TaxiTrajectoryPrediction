
# Taxi Trajectory Prediction

This is one of the two competitions in ECML-PKDD 2015.

## Data preprocessing

1. Find the boundary of all the trajectories in terms of a square region.
   1. This is achieved by the python scripts `Preprocessing/Bins/find_boundary.py`.
   1. The result is in the file `Preprocessing/Results/boundary`.
   1. The square region is defined by `-8.729766,-7.542072,41.062563,41.562351`.
1. Map GPS coordinate onto a graph with nodes and edges
   1. Define blocks inside the boundary
   1. The block is defined as a 100m X 100m square. Each block is a potential node in the underlying graph.
   1. Map points in the trajectories into nodes.
   1. Mapping reults
      |Block size|Difference in GPS|#Nodes|#Edges|
      |---:|---:|---:|
      |||
      |||

## Other information
1. Some statistics about data

   | Number of Training records | Number of test records|
   |---:|---:|
   |1710670 | 320 |
 
1. Relationship between coordinate and distance

   |Different in coordinate|Distance in km|
   |-----:|-----|
   |0.001   |0.1   |
   |0.0001  |0.01  |
   |0.00001 |0.001 |
