demand_df = pd.read_csv('/Users/shantanuraut/Desktop/Shell.Ai/Demand_History.csv')
EV_inf_2018_df = pd.read_csv('/Users/shantanuraut/Desktop/Shell.Ai/exisiting_EV_infrastructure_2018.csv')

def sort_demand_point_with_distance(x1,y,l,d):
  i=0
  for x in l:
    if d[x]>y:
      l.insert(i,x1)
      break
    if(x==l[-1]):
      l.append(x1)
      break
    i+=1
  if(len(l)==0):
    l.append(x1)


import math
def Euclidean_distance(p1,p2):
  return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

L=[]
D={}
for i in range(len(demand_df)):
  x1=demand_df.iloc[i]['x_coordinate']
  y1=demand_df.iloc[i]['y_coordinate']
  d_index=demand_df.iloc[i]['demand_point_index']
  if(i%400==0):
    print(i)
  for j in range(len(EV_inf_2018_df)):
    # print(i,j)
    x2=EV_inf_2018_df.iloc[j]['x_coordinate']
    y2=EV_inf_2018_df.iloc[j]['y_coordinate']
    p_index=EV_inf_2018_df.iloc[j]['supply_point_index']
    distance=Euclidean_distance((x1,y1),(x2,y2))
    D[(d_index,p_index)]=distance
    sort_demand_point_with_distance((d_index,p_index),distance,L,D)

d={}
l=[]
for x in L:
  l.append(D[x])
d['pair']=L
d['distance']=l

d=pd.DataFrame(d)
d.to_csv('/Users/shantanuraut/Desktop/Shell.Ai/sorted_pair.csv')
