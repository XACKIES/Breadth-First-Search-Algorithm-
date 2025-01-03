# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HXhrEQCXegRv_bsoFXdA0-FG0yoOfuS4
"""

#           Map(Distance)
#
#    A----D1-----B----D2-----C
#    |           |           |
#    D3          D4          D5
#    |           |           |
#    D----D6-----E----D7-----F
#    |           |           |
#    D8          D9          D10
#    |           |           |
#    G----D11----H----D12----I




#           Map(Time)
#
#    A----T1-----B----T2-----C
#    |           |           |
#    T3          T4          T5
#    |           |           |
#    D----T6-----E----D7-----F
#    |           |           |
#    T8          T9          T10
#    |           |           |
#    G----T11----H----T12----I



# Library 
import random


#Define Data

##D1  = random.randrange(1,21) 
##D2  = random.randrange(1,21) 
##D3  = random.randrange(1,21) 
##D4  = random.randrange(1,21) 
##D5  = random.randrange(1,21) 
##D6  = random.randrange(1,21) 
##D7  = random.randrange(1,21) 
##D8  = random.randrange(1,21) 
##D9  = random.randrange(1,21) 
##D10 = random.randrange(1,21) 
##D11 = random.randrange(1,21) 
##D12 = random.randrange(1,21) 
##
##
##T1  = random.randrange(1,21) 
##T2  = random.randrange(1,21) 
##T3  = random.randrange(1,21) 
##T4  = random.randrange(1,21) 
##T5  = random.randrange(1,21) 
##T6  = random.randrange(1,21) 
##T7  = random.randrange(1,21) 
##T8  = random.randrange(1,21) 
##T9  = random.randrange(1,21) 
##T10 = random.randrange(1,21) 
##T11 = random.randrange(1,21) 
##T12 = random.randrange(1,21)

D1  =  11 
D2  =  8 
D3  =  20 
D4  =  15 
D5  =  17 
D6  =  3 
D7  =  11 
D8  =  11 
D9  =  19 
D10 =  5 
D11 =  8 
D12 =  5 

T1  =  3 
T2  =  12 
T3  =  1 
T4  =  19 
T5  =  5 
T6  =  11 
T7  =  17 
T8  =  14 
T9  =  15 
T10 =  20 
T11 =  1 
T12 =  4


print\
(\
"D1  = ",D1  ,'\n'
"D2  = ",D2  ,'\n'\
"D3  = ",D3  ,'\n'\
"D4  = ",D4  ,'\n'\
"D5  = ",D5  ,'\n'\
"D6  = ",D6  ,'\n'\
"D7  = ",D7  ,'\n'\
"D8  = ",D8  ,'\n'\
"D9  = ",D9  ,'\n'\
"D10 = ",D10 ,'\n'\
"D11 = ",D11 ,'\n'\
"D12 = ",D12 ,'\n'\
)

print\
(\
"T1  = ",T1  ,'\n'
"T2  = ",T2  ,'\n'\
"T3  = ",T3  ,'\n'\
"T4  = ",T4  ,'\n'\
"T5  = ",T5  ,'\n'\
"T6  = ",T6  ,'\n'\
"T7  = ",T7  ,'\n'\
"T8  = ",T8  ,'\n'\
"T9  = ",T9  ,'\n'\
"T10 = ",T10 ,'\n'\
"T11 = ",T11 ,'\n'\
"T12 = ",T12 ,'\n'\
)

# Adgency List
##connections = { 'A' : [('B',D1,T1), ('D',D2,T2)],                                       
##                'B' : [('A',D1,T1), ('C',D3,T3), ('E',D4,T4)],
##                'C' : [('B',D3,T3), ('F',D5,T5)],                                       
##                'D' : [('A',D2,T2), ('E',D6,T6), ('G',D7,T7)],
##                'E' : [('B',D4,T4), ('D',D6,T6), ('F',D8,T8), ('H',D9,T9)],    
##                'F' : [('C',D5,T5), ('E',D8,T8), ('I',D10,T10)],
##                'G' : [('D',D7,T7), ('H',D11,T11)],                                   
##                'H' : [('E',D9,T9), ('G',D11,T11), ('I',D12,T12)],
##                'I' : [('F',D10,T10), ('H',D12,T12)] }

connections = { 'A': [ ('B',D1,T1)  , ('D',D3,T3) ],
                'B': [ ('A',D1,T1)  , ('C',D2,T2) , ('E',D4,T4) ],
                'C': [ ('B',D2,T2)  , ('F',D5,T5) ],
                'D': [ ('A',D3,T3)  , ('E',D6,T6) , ('G',D8,T8) ],
                'E': [ ('B',D4,T4)  , ('D',D6,T6) , ('F',D7,T7) , ('H',D9,T9) ],
                'F': [ ('C',D5,T5)  , ('E',D7,T7) , ('I',D10,T10)],
                'G': [ ('D',D8,T8)  , ('H',D11,T11)],
                'H': [ ('E',D9,T9)  , ('G',D11,T11), ('I',D12,T12)],
                'I': [ ('F',D10,T10), ('H',D12,T12)] }

# Action choice
actions = [0, 1, 2, 3]

# Function for Algorithm

def NextNode(n,a):
    if a >= len(connections[n]):
        return n,0,0
    else:
        return  connections[n][a][0] , connections[n][a][1], connections[n][a][2]

def TargetFound(node ,target = 'I'):  # default value is 'I'
  if node == target:
    return True
  else :
    return False

# Class NodePath for Algorithm Search

class NodePath :
    
    def __init__(self,action,node,parent,Distance,TimeD,energy,cost):
        self.action   = action
        self.node     = node
        self.parent   = parent

        self.each_distance = Distance
        self.each_time     = TimeD
        self.each_cost     = cost
        self.each_energy   = energy

        if self.parent :     # SUM distance which that passed

          self.distance = self.parent.distance + Distance
          self.Time     = self.parent.Time + TimeD
          self.cost     = self.parent.cost + cost
          self.energy   = self.parent.energy + energy

        else :               # Intitial distance 
          self.distance = Distance
          self.Time     = TimeD
          self.cost     = cost
          self.energy   = energy

    def Path(self):
        if self.parent == None:
            return ["Start Node :" + str((self.action,self.node))]
        else:
            return self.parent.Path()+[ ("Distance :" + str(self.distance) 
                                        ,"Each_distance :" + str(self.each_distance) 
                                        ,"Time tarvel :" + str(self.Time) 
                                        ,"Each_time :" + str(self.each_time) 
                                        ,"Action:"+ str(self.action) 
                                        ,str(self.parent.node) + " - To -> " + str(self.node)) 
                                        ,str(self.parent.ShortPath())  + str(self.node)]            
    def ShortPath(self):
        if self.parent == None:
            return self.node
        else:
            return self.parent.ShortPath()+self.node
        
    def inPath(self,n):
        if self.node == n:
            return True
        elif self.parent == None:
            return False
        else:
            return self.parent.inPath(n)

#A-->D-->E-->F-->I

# Class Queue for Algorithm Search

class Queue():             
 
  def __init__(self,choice):
    self.data      = []
    self.choice    = choice

  def push(self,node,dis,dtime,energy,cost):

    self.data.append((node,dis,dtime,energy,cost))
    #                  0    1    2     3      4

  def pop(self):

    if self.choice == 1:    # Choice 1 (Distance)
      m = []
      for i in range(len(self.data)):
        m.append(self.data[i][1])
      d = m.index(min(m))
      dd  = self.data[d][0]
      self.data.pop(d)    
      return dd

    if self.choice == 2:    # Choice 2 (Time)
      n = []
      for i in range(len(self.data)):
        n.append(self.data[i][2])
      t = n.index(min(n))
      tt  = self.data[t][0]
      self.data.pop(t)    
      return tt

    if self.choice == 3:    # Choice 3 (Energy)
      o  = [] 
      for i in range(len(self.data)):
        o.append(self.data[i][3])
      e  = o.index(min(o))
      ee  = self.data[e][0]
      self.data.pop(e)    
      return ee
    
    if self.choice == 4:    # Choice 4 (Cost)
      p  = [] 
      for i in range(len(self.data)):
        p.append(self.data[i][4])
      c   = p.index(min(p))
      cc  = self.data[c][0]
      self.data.pop(c)   
      return cc


  def empty(self):
    if self.data == [] :
      return True 
    else :
      return False

#  Algorithm of Function 

def Breadth_First_Search(Show_step,initialNode , NodeFound  ,action , Nextnode , choice   ,cost_time = 1 ,cost_dis = 1):
  
  if TargetFound(initialNode,NodeFound):
    return ["Still at the same place :  " + str(initialNode)]
  Start_Path = NodePath(None,initialNode,None,0,0,0,0)

  q = Queue(choice)

  q.push(Start_Path,0,0,0,0)

  Mock_Queue = [(initialNode,0,0)]
  if Show_step == 1: print('Mock_Queue : ',Mock_Queue)

  m =[]
  while not q.empty():

    p = q.pop()
  
    for j in actions :

      New_node,dis,time = Nextnode(p.node,j)

      if not p.inPath(New_node):
        energy   = float("%.2f "%(((dis/time)**2)))
        cost     = (dis*cost_dis)+(time*cost_time)
        New_path = NodePath( j , New_node , p , dis , time , energy ,cost )
        q.push            (New_path            ,New_path.distance ,New_path.Time,New_path.energy,New_path.cost)
        Mock_Queue.append((New_path.ShortPath(),New_path.distance ,New_path.Time,New_path.energy,New_path.cost ))

      if TargetFound(p.node,NodeFound):
        #p = q.pop()
        return p#.Path()

    for i in range(len(Mock_Queue)):
            m.append(Mock_Queue[i][1])
            c = m.index(min(m))
    if Show_step == 1: print('Expanding -->',Mock_Queue.pop(c)[0])
    if Show_step == 1: print('Mock_Queue : ',Mock_Queue)
    m = []
    if Show_step == 1: print('---------------------------------')
  return None

def int_in(text):
    while True:
        user_in = input(text)
        try:
            out = int(user_in)
            if out >= 0:
                return out
                break
            print('INPUT -  Again,please')
        except:
            print('INPUT -  Again,please')

print('\n'*5)#Space
print("Start --  Program")
print(    )#Space


while True:
    

    print ("\
                  Map\n\
\n\
    A---( D1 , T1 )---B---( D2 , T2 )---C\n\
    |                 |                 |\n\
    |                 |                 |\n\
 (D3,T3)           (D4,T4)           (D5,T5)\n\
    |                 |                 |\n\
    |                 |                 |\n\
    D---( D6 , T6 )---E---( D7 , T7 )---F\n\
    |                 |                 |\n\
    |                 |                 |\n\
 (D8,T8)           (D9,T9)          (D10,10)\n\
    |                 |                 |\n\
    |                 |                 |\n\
    G---( D11,T11 )---H---( D12,T12 )---I\n\
")
    print ("\
                  Map\n\
\n\
    A---(",D1,',',T1,")---B---(",D2,',',T2,")---C\n\
    |               |               |\n\
    |               |               |\n\
(",D3,',',T3,")     (",D4,',',T4,")      (",D5,',',T5,")\n\
    |               |               |\n\
    |               |               |\n\
    D---(",D6,',',T6,")---E---(",D7,',',T7,")---F\n\
    |               |               |\n\
    |               |               |\n\
(",D8,',',T8,")    (",D9,',',T9,")       (",D10,',',T10,")\n\
    |               |               |\n\
    |               |               |\n\
    G---(",D11,',',T11,")---H---(",D12,',',T12,")---I\n\
")
    
    setting    = 0
    Final_Node = 'I' 
    # Configuration testing
    
    print("Select Choice")
    print(    )#Space
    print("  1 - Distance")
    print("  2 - Time    ")
    print("  3 - Energy    ")
    print("  4 - Cost   ")
    print(    )#Space
    
    R  =  [ e for e in input("Choice:").split() ]
    
    cost_time = int_in("Cost_time : ")
    cost_dis  = int_in("Cost_dis  : ")
    
    if len(R)>1 :
        
        if  R[1].isnumeric() == True  :
            
            print("Show Back End")
            print("\n"*3)
            setting = 1

        if  R[1].isnumeric() == False :
            print(  )#Space
            print("Find Node :", R[1] , "in Map")
            
            Final_Node = R[1]
        

    print('\n==>Output : ')#Space
    d = Breadth_First_Search(setting,'A',Final_Node,actions,NextNode,int(R[0]),cost_time ,cost_dis)
    
    
    if d == None:
      print("Not Found :", Final_Node," in Map")
    if d != None:
      a = d.Path()

      for j in range(len(a)):
        print(a[j])
      #   short_path , distance , time , ,energy,cost 
      print('Total Distance : ' , d.distance)
      print('Total Time     : ' , d.Time)
      print('Total Energy   : ' , d.energy)
      print('Total cost     : ' , d.cost)
      
    print(  )#Space
    print(  )#Space
    print("What's Next ?")
    print("  1 - Continue")
    print("  2 - Close Program   ")
    Whats_up = int_in("Choose : ")
    if Whats_up == 2 :
        break
    print('\n'*5)#Space
print("it's time to let go ,Bye :)")
print(  )#Space
print("====== Close Program ======")
#exit()
