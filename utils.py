from collections import deque


def create_node(state, parent, action, path_cost, depth):
    return (state, parent, action, path_cost, depth)


def print_solution(n):
  print()
  print("######Solution######")
  j = 0
  r = deque()
  while n is not None:
    for slist in n[0]:
      while(len(slist)<4):
        slist.insert(0,".")
    r.appendleft(n[0])
    n = n[1]
  for s in r:
    print("Step",j)
    for i in range(4):
      print(s[0][i],end=" ")
      print(s[1][i],end=" ")
      print(s[2][i],end=" ")
      print(s[3][i],end=" ")
      print(s[4][i],end=" ")
      print(s[5][i],end=" ")
      print()
    print()
    j += 1
