from collections import deque

class Station:
    def __init__(self,name):
        self.name=name
        self.neighbors=[]
    def add_connection(self,another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)

def bfs(start,goal):
    previous={}
    queue=deque()
    current=None

    previous[start]=None
    queue.append(start)

    while len(queue)>0 and current!=goal:
        current=queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor]=current

    if current==goal:
        path=[goal]
        x=goal

        while previous[x]!=None:
            x=previous[x]
            path.append(x)

    return path

stations={}
in_file=open("stations.txt",'rt',encoding='UTF-8')

for line in in_file:
    print(line)
    previous_station=None
    data=line.strip().split("-")
    for name in data:
        station_name=name.strip()
        if station_name not in stations.keys():
            current_station=Station(station_name)
            stations[station_name]=current_station
            print(stations)
        else:
            current_station=stations[station_name]
            print(current_station)

        if previous_station!=None:
            current_station.add_connection(previous_station)
            print(current_station)

        previous_station=current_station

in_file.close()

start_name="잠실"
goal_name="소요산"

start=stations[start_name]
goal=stations[goal_name]

path=bfs(start,goal)

for station in path:
    print(station.name)