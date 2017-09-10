# Quick-Find-and-Quick-Union-Algorithm
Improvement on run time of Quick Find and Quick Union Algorithm.

Quick Find:
In a network with N nodes, Quick Find is the algorithm to find out if the nodes p and q are connected.

Quick Union:
In a network with N nodes, Quick Union is the algorithm to unite two nodes p and q.

The network can be realized as a integer array of size N where the nodes have their entries intialized to their index. The nodes p and q are connected if and only if they have the same entry. 
For example:
  if we give Union(p,q), the node p gets connected with q.
  
Implementation of this algorithm using eager approach takes (N * N) access for union operation and quick find takes N times.
Since the uion operation is quadratic which is very expensive we try to improve the algorithm by using Lazy approach where each entry in the array is the root of that element. so multiple entry changes does not take place. 
This algorithm improves the run time to N times for both quick union and quick find.
The Lazy approach is still slow and takes more access time when the tree is tall.
The Flat approach is the new algorithm that improves the union and find to Log N (base 2)
In the flat approach, while union operation the small tree is combined with the large tree. This makes the depth of any node almost equal to lg N.
  
The developed algorithm is included in the code file.
The quickeager.py is the python code to realized the quick eager approach
The quicklazy.py is the python code to realize the quick Lazy approach
The quickflat.py is the python code to realize the quick Flat approach.
