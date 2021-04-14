
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()  # Set to keep track of visited nodes.
        graph = employees
        node = id
        employee_importance = 0
        self.dfs(employee_importance, visited, graph, node)
        return employee_importance

    def dfs(self, employee_importance, visited, graph, node):
        if node not in visited:
            print(node)
            visited.add(node)
        for neighbour in graph[node]:
            employee_importance = employee_importance + neighbour.importance
            self.dfs(employee_importance, visited, graph, neighbour)
