### Pizza Bot Simulator
This applications simulates a pizza bot dropping off pizzas to a provided list of waypoints in a grid representing a cartesian plane. The application can be run both manually from a command prompt or via some simple examples provided in the Makefile. This application requires at least python 3.5.

The application consists of 2 primary files:
1. pizzabot.py (main application)
2. pizza_bot_tests.py (unit tests)

The application makes use of a simple BFS traversal to find the path from the starting coordinate to all of the provided drop off points. Since the directions stated that finding an optimal path was not a priority BFS was chosen over implementing something like A* with a Manhattan distance heuristic. In a real world scenario where finding the shortest path to deliver pizzas would be beneficial a better algorithm would be appropriate. 

#### Running application manually
`python3 pizzabot.py WxH (xCoord, yCoord)`

#### Running application from Makefile
`make simple-example` or `make full-example`

#### Unit tests
Unit tests have been included and can be run with `make test`