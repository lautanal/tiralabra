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


    def test_test_siksak_sama_tulos(self):
        costs = [['1','1','2','2','2','2'],
                ['2','1','1','1','2','2'],
                ['2','2','2','1','1','1'],
                ['2','2','2','2','2','1'],
                ['2','2','2','2','2','1'],
                ['2','1','1','1','1','1']]
        self.initmap(costs)

        res1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res2 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res3 = self.algorithm.calculate()
        self.assertEqual((res1[1] == 9 and res2[1] == 9 and res3[1] == 9), True)


    def test_metodit_eivat_loyda_reittia(self):
        costs = [['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['1','1','1','1','1','1'],
                    ['B','B','B','B','B','B'],
                    ['1','1','1','1','1','1']]
        self.initmap(costs)

        self.algorithm.set_diagonal()
        self.algorithm.set_diagonal()
        res1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res2 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res3 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.assertEqual((res1[0] and res2[0] and res3[0]), False)


    def test_diagonaalireitti_sama_tulos(self):
        costs = [['1','2','2','2','2','2'],
                ['2','1','2','2','2','2'],
                ['2','2','1','2','2','2'],
                ['2','2','2','1','2','2'],
                ['2','2','2','2','1','2'],
                ['2','2','2','2','2','1']]
        self.initmap(costs)

        self.algorithm.set_diagonal()
        self.algorithm.set_animate()
        self.algorithm.set_animate()
        res1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res2 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        res3 = self.algorithm.calculate()
        self.assertEqual((res1[1] == 4 and res2[1] == 4 and res3[1] == 4),True)


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

        node = self.map.nodes[3][0]
        node.clear()
        node.reset_color()
        node.set_blocked()
        self.algorithm.set_method()
        self.algorithm.set_method()
        result = self.algorithm.calculate()
        self.assertEqual(result[2], 12)


    def test_dijkstra_astar_random_sama_tulos(self):
        self.initmap(None)

        result1 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.map.reset()
        result2 = self.algorithm.calculate()
        self.algorithm.set_method()
        self.algorithm.set_method()
        self.assertEqual(result1[2], result2[2])
