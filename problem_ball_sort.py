global initial_state

def is_goal_state(state_list):
  if(["A","A","A","A"] in state_list and ["B","B","B","B"] in state_list and ["C","C","C","C"] in state_list and ["D","D","D","D"] in state_list):
    return True
  else:
    return False
  
def set_initial_state(s1,s2,s3,s4,s5,s6):
  global initial_state
  initial_state = [s1,s2,s3,s4,s5,s6]

def get_initial_state():
  global initial_state
  return initial_state

def successors(state):
  s1,s2,s3,s4,s5,s6 = state
  #if stack already correct we do not move it
  s1_is_correct = False
  s2_is_correct = False
  s3_is_correct = False
  s4_is_correct = False
  s5_is_correct = False
  s6_is_correct = False
  if(len(s1) == 4):
    if(s1[0] == s1[1] == s1[2] == s1[3]):
      s1_is_correct = True
  if(len(s2) == 4):
    if(s2[0] == s2[1] == s2[2] == s2[3]):
      s2_is_correct = True
  if(len(s3) == 4):
    if(s3[0] == s3[1] == s3[2] == s3[3]):
      s3_is_correct = True
  if(len(s4) == 4):
    if(s4[0] == s4[1] == s4[2] == s4[3]):
      s4_is_correct = True
  if(len(s5) == 4):
    if(s5[0] == s5[1] == s5[2] == s5[3]):
      s5_is_correct = True
  if(len(s6) == 4):
    if(s6[0] == s6[1] == s6[2] == s6[3]):
      s6_is_correct = True
  #s1 to another stack
  if(len(s1)>0 and not s1_is_correct):
    #s1-->s2
    if(not s2):
      yield [s1[1:],[s1[0]]+s2,s3,s4,s5,s6] , 1
    elif(len(s2)<4 and s1[0] == s2[0] ):
      yield [s1[1:],[s1[0]]+s2,s3,s4,s5,s6] , 1
    #s1-->s3
    if(not s3):
      yield [s1[1:],s2,[s1[0]]+s3,s4,s5,s6] , 1
    elif(len(s3)<4 and s1[0] == s3[0]):
      yield [s1[1:],s2,[s1[0]]+s3,s4,s5,s6] , 1
    #s1-->s4
    if(not s4):
       yield [s1[1:],s2,s3,[s1[0]]+s4,s5,s6] , 1      
    elif(len(s4)<4 and s1[0] == s4[0]):
      yield [s1[1:],s2,s3,[s1[0]]+s4,s5,s6] , 1
    #s1-->s5
    if(not s5):
      yield [s1[1:],s2,s3,s4,[s1[0]]+s5,s6] , 1
    elif(len(s5)<4 and s1[0] == s5[0]):
      yield [s1[1:],s2,s3,s4,[s1[0]]+s5,s6] , 1
    #s1-->s6
    if(not s6):
      yield [s1[1:],s2,s3,s4,s5,[s1[0]]+s6] , 1
    elif(len(s6)<4 and s1[0] == s6[0]):
      yield [s1[1:],s2,s3,s4,s5,[s1[0]]+s6] , 1
  #s2 to another stack
  if(len(s2)>0 and not s2_is_correct):
    #s2-->s1
    if(not s1):
      yield [[s2[0]]+s1,s2[1:],s3,s4,s5,s6] , 1
    elif(len(s1)<4 and s2[0] == s1[0] ):
      yield [[s2[0]]+s1,s2[1:],s3,s4,s5,s6] , 1
    #s2-->s3
    if(not s3):
       yield [s1,s2[1:],[s2[0]]+s3,s4,s5,s6] , 1
    elif(len(s3)<4 and s2[0] == s3[0]):
      yield [s1,s2[1:],[s2[0]]+s3,s4,s5,s6] , 1
    #s2-->s4
    if(not s4):
      yield [s1,s2[1:],s3,[s2[0]]+s4,s5,s6] , 1
    elif(len(s4)<4 and s2[0] == s4[0] ):
      yield [s1,s2[1:],s3,[s2[0]]+s4,s5,s6] , 1
    #s2-->s5
    if(not s5):
      yield [s1,s2[1:],s3,s4,[s2[0]]+s5,s6] , 1
    elif(len(s5)<4 and s2[0] == s5[0] ):
      yield [s1,s2[1:],s3,s4,[s2[0]]+s5,s6] , 1
    #s2-->s6
    if(not s6):
      yield [s1,s2[1:],s3,s4,s5,[s2[0]]+s6] , 1
    elif(len(s6)<4 and s2[0] == s6[0]):
      yield [s1,s2[1:],s3,s4,s5,[s2[0]]+s6] , 1
  #s3 to another stack
  if(len(s3)>0 and not s3_is_correct):
    #s3-->s1
    if(not s1):
      yield [[s3[0]]+s1,s2,s3[1:],s4,s5,s6] , 1
    elif(len(s1)<4 and s3[0] == s1[0]):
      yield [[s3[0]]+s1,s2,s3[1:],s4,s5,s6] , 1
    #s3-->s2
    if(not s2):
      yield [s1,[s3[0]]+s2,s3[1:],s4,s5,s6] , 1
    elif(len(s2)<4 and s3[0] == s2[0]):
      yield [s1,[s3[0]]+s2,s3[1:],s4,s5,s6] , 1
    #s3-->s4
    if(not s4):
      yield [s1,s2,s3[1:],[s3[0]]+s4,s5,s6] , 1
    elif(len(s4)<4 and s3[0] == s4[0]):
      yield [s1,s2,s3[1:],[s3[0]]+s4,s5,s6] , 1
    #s3-->s5
    if(not s5):
      yield [s1,s2,s3[1:],s4,[s3[0]]+s5,s6] , 1
    elif(len(s5)<4 and s3[0] == s5[0]):
      yield [s1,s2,s3[1:],s4,[s3[0]]+s5,s6] , 1
    #s3-->s6
    if(not s6):
      yield [s1,s2,s3[1:],s4,s5,[s3[0]]+s6] , 1
    elif(len(s6)<4 and s3[0] == s6[0]):
      yield [s1,s2,s3[1:],s4,s5,[s3[0]]+s6] , 1
  #s4 to another stack
  if(len(s4)>0 and not s4_is_correct):
    #s4-->s1
    if(not s1):
      yield [[s4[0]]+s1,s2,s3,s4[1:],s5,s6] , 1
    elif(len(s1)<4 and s4[0] == s1[0]):
      yield [[s4[0]]+s1,s2,s3,s4[1:],s5,s6] , 1
    #s4-->s2
    if(not s2):
      yield [s1,[s4[0]]+s2,s3,s4[1:],s5,s6] , 1
    elif(len(s2)<4 and s4[0] == s2[0]):
      yield [s1,[s4[0]]+s2,s3,s4[1:],s5,s6] , 1
    #s4-->s3
    if(not s3):
      yield [s1,s2,[s4[0]]+s3,s4[1:],s5,s6] , 1
    elif(len(s3)<4 and s4[0] == s3[0]):
      yield [s1,s2,[s4[0]]+s3,s4[1:],s5,s6] , 1
    #s4-->s5
    if(not s5):
      yield [s1,s2,s3,s4[1:],[s4[0]]+s5,s6] , 1
    elif(len(s5)<4 and s4[0] == s5[0]):
      yield [s1,s2,s3,s4[1:],[s4[0]]+s5,s6] , 1
    #s4-->s6
    if(not s6):
      yield [s1,s2,s3,s4[1:],s5,[s4[0]]+s6] , 1
    elif(len(s6)<4 and s4[0] == s6[0]):
      yield [s1,s2,s3,s4[1:],s5,[s4[0]]+s6] , 1
  #s5 to another stack
  if(len(s5)>0 and not s5_is_correct):
    #s5-->s1
    if(not s1):
      yield [[s5[0]]+s1,s2,s3,s4,s5[1:],s6] , 1
    elif(len(s1)<4 and s5[0] == s1[0]):
      yield [[s5[0]]+s1,s2,s3,s4,s5[1:],s6] , 1
    #s5-->s2
    if(not s2):
      yield [s1,[s5[0]]+s2,s3,s4,s5[1:],s6] , 1
    elif(len(s2)<4 and s5[0] == s2[0]):
      yield [s1,[s5[0]]+s2,s3,s4,s5[1:],s6] , 1
    #s5-->s3
    if(not s3):
      yield [s1,s2,[s5[0]]+s3,s4,s5[1:],s6] , 1
    elif(len(s3)<4 and s5[0] == s3[0]):
      yield [s1,s2,[s5[0]]+s3,s4,s5[1:],s6] , 1
    #s5-->s4
    if(not s4):
      yield [s1,s2,s3,[s5[0]]+s4,s5[1:],s6] , 1
    elif(len(s4)<4 and s5[0] == s4[0]):
      yield [s1,s2,s3,[s5[0]]+s4,s5[1:],s6] , 1
    #s5-->s6
    if(not s6):
      yield [s1,s2,s3,s4,s5[1:],[s5[0]]+s6] , 1
    elif(len(s6)<4 and s5[0] == s6[0]):
      yield [s1,s2,s3,s4,s5[1:],[s5[0]]+s6] , 1
  #s6 to another stack
  if(len(s6)>0 and not s6_is_correct):
    #s6-->s1
    if(not s1):
      yield [[s6[0]]+s1,s2,s3,s4,s5,s6[1:]] , 1
    elif(len(s1)<4 and s6[0] == s1[0]):
      yield [[s6[0]]+s1,s2,s3,s4,s5,s6[1:]] , 1
    #s6-->s2
    if(not s2):
      yield [s1,[s6[0]]+s2,s3,s4,s5,s6[1:]] , 1
    elif(len(s2)<4 and s6[0] == s2[0]):
      yield [s1,[s6[0]]+s2,s3,s4,s5,s6[1:]] , 1
    #s6-->s3
    if(not s3):
      yield [s1,s2,[s6[0]]+s3,s4,s5,s6[1:]] , 1
    elif(len(s3)<4 and s6[0] == s3[0]):
      yield [s1,s2,[s6[0]]+s3,s4,s5,s6[1:]] , 1
    #s6-->s4
    if(not s4):
      yield [s1,s2,s3,[s6[0]]+s4,s5,s6[1:]] , 1
    elif(len(s4)<4 and s6[0] == s4[0]):
      yield [s1,s2,s3,[s6[0]]+s4,s5,s6[1:]] , 1
    #s6-->s5
    if(not s5):
      yield [s1,s2,s3,s4,[s6[0]]+s5,s6[1:]] , 1
    elif(len(s5)<4 and s6[0] == s5[0]):
      yield [s1,s2,s3,s4,[s6[0]]+s5,s6[1:]] , 1
