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


    def test_test_siksak(self):
        costs = [['1','1','2','2','2','2'],
                ['2','1','1','1','2','2'],
                ['2','2','2','1','1','1'],
                ['2','2','2','2','2','1'],
                ['2','2','2','2','2','1'],
                ['2','1','1','1','1','1']]
        self.initmap(costs)

        result = self.algorithm.calculate()
        self.assertEqual(result[1], 9)


    def test_ei_loyda_reittia(self):
        costs = [['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['B','B','B','B','B','B'],
                    ['1','1','1','1','1','1']]
        self.initmap(costs)

        result = self.algorithm.calculate()
        self.assertEqual(result[0], False)


    def test_dijkstra_diagonaalireitti(self):
        costs = [['1','2','2','2','2','2'],
                ['2','1','2','2','2','2'],
                ['2','2','1','2','2','2'],
                ['2','2','2','1','2','2'],
                ['2','2','2','2','1','2'],
                ['2','2','2','2','2','1']]
        self.initmap(costs)

        self.algorithm.set_diagonal()
        result = self.algorithm.calculate()
        self.assertEqual(result[1],4)


    def test_astar_diagonaalireitti(self):
        costs = [['1','2','2','2','2','2'],
                ['1','2','2','2','2','2'],
                ['2','1','1','2','2','2'],
                ['2','2','2','1','2','2'],
                ['2','2','2','2','1','2'],
                ['2','2','2','2','2','1']]
        self.initmap(costs)

        self.algorithm.set_method()
        self.algorithm.set_diagonal()
        result = self.algorithm.calculate()
        self.assertEqual(result[1],5)


    def test_idastar_paras_reitti(self):
        costs = [['1','1','1','1','1','1'],
                ['1','1','1','1','1','1'],
                ['1','1','1','1','1','1'],
                ['B','8','B','6','B','4'],
                ['1','1','1','1','1','1'],
                ['1','1','1','1','1','1']]
        self.initmap(costs)

        self.algorithm.set_method()
        self.algorithm.set_method()
        result = self.algorithm.calculate()
        self.assertEqual(result[2], 12)


    def test_dijkstra_astar_sama_tulos(self):
        self.initmap(None)

        result1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        result2 = self.algorithm.calculate()
        self.assertEqual(result1[2], result2[2])
