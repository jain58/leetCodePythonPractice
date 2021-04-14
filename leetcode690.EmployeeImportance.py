from typing import List

import typing.List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()  # Set to keep track of visited nodes.
        self.employee_importance = 0
        self.employee_importance = self.dfs(self.employee_importance, visited, employees, id)
        return self.employee_importance

    def dfs(self, employee_importance, visited, employees, node):
        if node not in visited:
            visited.add(node)
            selectedEmployee = [employee for employee in employees if employee.id == node]
            if selectedEmployee is not None:
                self.employee_importance = self.employee_importance + selectedEmployee[0].importance
                for neighbour in selectedEmployee[0].subordinates:
                    self.dfs(employee_importance, visited, employees, neighbour)
        return self.employee_importance