import unittest
from map import Map
from node import Node
from algorithm import Algorithm

class TestBestroute(unittest.TestCase):
    def initmap(self, costs):
        if costs:
            nrows = len(costs)
            ncols = len(costs[0])
        else:
            nrows = 20
            ncols = 20
        self.map = Map(nrows, ncols, 10)
        if costs:
            self.map.set_costs(costs)
        else:
            self.map.generate_costs()
        self.algorithm = Algorithm(self.map, None)
        node = self.map.nodes[0][0]
        node.set_start()
        self.map.set_start(node)
        node = self.map.nodes[nrows-1][ncols-1]
        node.set_goal()
        self.map.set_goal(node)


    def test_map1(self):
        costs = [['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1']]
        self.initmap(costs)

        result = self.algorithm.calculate()
        self.assertEqual(result[1], 9)


    def test_map2(self):
        costs = [['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['B','B','B','B','B','B'],
                    ['1','1','1','1','1','1']]
        self.initmap(costs)

        result = self.algorithm.calculate()
        self.assertEqual(result[0], False)


    def test_map3(self):
        costs = [['1','1','2','2','2','2'],
                    ['2','1','1','2','2','2'],
                    ['2','2','1','1','2','2'],
                    ['2','2','2','1','2','2'],
                    ['2','2','2','1','1','2'],
                    ['2','2','2','2','4','1']]
        self.initmap(costs)

        result1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        result2 = self.algorithm.calculate()
        self.assertEqual(result1[2], result2[2])


    def test_map4(self):
        costs = [['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['B','3','B','2','B','4'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1']]
        self.initmap(costs)

        self.algorithm.set_method()
        self.algorithm.set_method()
        self.map.reset()
        result = self.algorithm.calculate()
        self.assertEqual(result[2], 10)


    def test_map5(self):
        self.initmap(None)

        self.algorithm.set_diagonal()
        result1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        result2 = self.algorithm.calculate()
        self.assertEqual(result1[2], result2[2])
