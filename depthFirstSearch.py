# Using a Python dictionary to act as an adjacency list
from typing import List

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'B')


# 1. Create a list of dictionaries
users = [{'username': 'alice', 'age': 23, 'play_time': 101},
         {'username': 'bob', 'age': 31, 'play_time': 88},
         {'username': 'ann', 'age': 25, 'play_time': 121},]

# Use list comprehension to filter out the dictionaries that
# don't meet a certain condition ('play_time'>100)
superplayers = [user for user in users if user['play_time']>100]

# Print the result to the shell
print(superplayers)


json = [
    {
        "user": "alice",
        "type": "free"
    },
    {
        "user": "ann",
        "type": "paid"
    },
    {
        "user": "bob",
        "type": "paid"
    }
]
filtered = [x for x in json if x['type']=='paid']
print(filtered)
# [{'user': 'ann', 'type': 'paid'},
#  {'user': 'bob', 'type': 'paid'}]

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]],
employees =[]
employees.append(Employee(1,5,[2,3]))
employees.append(Employee(2,3,[]))
employees.append(Employee(3,3,[]))
node =1
selectedEmployee = [employee for employee in employees if employee.id==node]
print(selectedEmployee[0])