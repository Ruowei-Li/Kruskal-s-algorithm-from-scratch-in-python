# Kruskals algorithm from scratch in python

This algorithm solves the minimum spanning tree (MST) problem. This is an implementation of the Kruskal algorithm for finding the minimum spanning tree from a sparse graph. The running time is O(m log n) for m edges and n nodes.

## Test case description


We use # for the comment and we have e.g. n = 5 to indicate the value n of number of nodes. The node index starts from 1. There is a whitespace after #, n, = to make the parsing process easily.

If there is an edge between two nodes x and y, there will be two lines with the format of x y w and y x w, where w is the weight of the edge between x and y. All weights w are non negative integers smaller than 1000. There is one whitespace between each integer on each line.

The output is the weight of the minimum spanning tree, i.e. the sum of weights given to each edge of the spanning tree.


## Sample Input:
```
# This is the a graph of n = 5. #
n=5
#
1 2 1
1 3 3
1 4 4
1 5 5
2 1 1
2 3 2
3 1 3
3 2 2
4 1 4
5 1 5
```

## Sample Output:
```
12
```
