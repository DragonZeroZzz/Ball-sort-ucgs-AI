import problem_ball_sort as pb
import uniform_cost_graph_search as ucgs
import utils

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []

for i in range(4):
  L = input("Type your initial state:").split(" ")
  stack1.append(L[0])
  stack2.append(L[1])
  stack3.append(L[2])
  stack4.append(L[3])

pb.set_initial_state(stack1,stack2,stack3,stack4,stack5,stack6)
pb.get_initial_state()
goal_node,n_visits = ucgs.uniform_cost_graph_search(pb)
if(goal_node == None):
  print("Cannot solve this Input.")
else:
  utils.print_solution(goal_node)
  print()
  print('Number of node visited:',n_visits)


