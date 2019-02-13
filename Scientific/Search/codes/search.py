import driver
from state import *

def search(start_state):

    explored, stack = set(), list([State(start_state, None, None, 0, 0, 0)])
    while stack:

        node = stack.pop()

        explored.add(node.map)

        if node.state == driver.goal_state:
            driver.goal_node = node
            return stack

        neighbors = reversed(driver.expand(node))

        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > driver.max_search_depth:
                    driver.max_search_depth += 1

        if len(stack) > driver.max_frontier_size:
            driver.max_frontier_size = len(stack)
