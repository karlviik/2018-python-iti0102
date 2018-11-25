"""Maze solver."""
from queue import PriorityQueue

MOVES = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class MazeSolver:
    """Solve a given maze."""

    def __init__(self, maze_str: str, configuration: dict = None):
        """
        Initialize the solver with map string and configuration.
        Map string can consist of several lines, line break separates the lines.
        Empty lines in the beginning and in the end should be ignored.
        Line can also consist of spaces, so the lines cannot be stripped.
        Map can have non-rectangular shape (# indicates the border of the line):

        #####
        #   #
        #  #
        # #
        ##

        On the left and right sides there can be several doors (marked with "|").
        Solving the maze starts from a door from the left side and ends at the door on the right side.
        See more @solve().

        Configuration is a dict which indicates which symbols in the map string have what cost.
        Doors (|) are not shown in the configuration and are not used inside the maze.
        Door cell cost is 0.
        When a symbol on the map string is not in configuration, its cost is 0.
        Cells with negative cost cannot be moved on/through.

        :param maze_str: Map string
        :param configuration: Optional dictionary of symbol costs.
        """
        if configuration is None:
            configuration = {
                ' ': 1,
                '#': -1,
                '.': 2,
                '-': 5,
                'w': 10
            }
        maze_lines = maze_str.splitlines()
        if maze_lines[0] == "":
            maze_lines.pop(0)
        if maze_lines[-1] == "":
            maze_lines.pop(-1)
        self.maze = []
        self.starts = []
        self.ends = []
        for x, line in enumerate(maze_lines):
            self.maze.append([])
            for y, symbol in enumerate(line):
                if symbol not in configuration.keys():
                    self.maze[x].append(0)
                    if symbol == "|":
                        if y == 0:
                            self.starts.append((x, y))
                        else:
                            self.ends.append((x, y))
                else:
                    self.maze[x].append(configuration[symbol])

    def isavalidcoord(self, x, y):
        """Given x and y coordinates, output True if the coord has no negative components and is traversable."""
        if 0 <= y < len(self.maze[x]) and 0 <= x < len(self.maze):
            if self.maze[x][y] >= 0:
                return True
        return False

    def get_shortest_path(self, start, goal):
        """
        Return shortest path and the total cost of it.

        The shortest path is the path which has the lowest cost.
        Start and end are tuples of (y, x) where the first (upper) line is y = 0.
        The path should include both the start and the end.

        If there is no path from the start to goal, the path is None and cost is -1.

        If there are several paths with the same lowest cost, return any of those.

        :param start: Starting cell (y, x)
        :param goal: Goal cell (y, x)
        :return: shortest_path, cost
        """

        def distance(a, b):
            ax, ay = a
            bx, by = b
            return abs(ax - bx) + abs(ay - by)

        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            currentcost, currentpos = frontier.get()

            if currentpos == goal:
                break

            for xdiff, ydiff in MOVES:
                x, y = currentpos
                xnew = x + xdiff
                ynew = y + ydiff
                newpos = (xnew, ynew)
                if self.isavalidcoord(xnew, ynew):
                    new_cost = cost_so_far[(x, y)] + self.maze[xnew][ynew]
                    if newpos not in cost_so_far or new_cost < cost_so_far[newpos]:
                        cost_so_far[newpos] = new_cost
                        priority = new_cost + distance(goal, newpos)
                        frontier.put((priority, newpos))
                        came_from[newpos] = currentpos
        if goal not in cost_so_far.keys():
            return None, -1
        else:
            path = [goal]
            pos = goal
            while pos is not start:
                path.append(came_from[pos])
                pos = came_from[pos]
            path.reverse()
            return path, cost_so_far[goal]

    def solve(self):
        """
        Solve the given maze and return the path and the cost.

        Finds the shortest path from one of the doors on the left side to the one of the doors on the right side.
        Shortest path is the one with the lowest cost.

        This method should use get_shortest_path method and return the same values.
        If there are several paths with the same cost, return any of those.

        :return: shortest_path, cost
        """
        bestpath, mincost = None, -1
        for startpos in self.starts:
            for endpos in self.ends:
                path, cost = self.get_shortest_path(startpos, endpos)
                if (cost < mincost and cost != -1) or mincost == -1:
                    mincost = cost
                    bestpath = path
        return bestpath, mincost
