#!/usr/bin/env python3
import unittest
import pizzabot


class TestPizzabot(unittest.TestCase):
    def test_check_args(self):
        self.assertRaises(SystemExit, pizzabot.check_args, "1234")
        self.assertTrue(pizzabot.check_args("5x5 (1, 3)"))

    def test_get_board_size(self):
        self.assertEqual(pizzabot.get_board_size('5x5'), (5, 5))
        self.assertNotEqual(pizzabot.get_board_size('4x4'), (5, 5))
        self.assertEqual((), pizzabot.get_board_size('axa'))

    def test_get_destination_coords(self):
        c = pizzabot.get_destination_coords(['0,0', '1,2', '2, 2'])
        self.assertEqual(len(c), 3)
        self.assertEqual(c[0], (0, 0, ''))
        self.assertEqual(c[1], (1, 2, ''))
        self.assertEqual(c[2], (2, 2, ''))
        c = pizzabot.get_destination_coords(['axa'])
        self.assertEqual(len(c), 0)

    def test_get_neighbors(self):
        grid = [[False for width in range(5)]
                for height in range(5)]
        n = pizzabot.get_neighbors((0, 0, ''), grid)
        self.assertEqual(len(n), 2)
        self.assertEqual(n[0], (1, 0, 'E'))
        self.assertEqual(n[1], (0, 1, 'N'))
        n = pizzabot.get_neighbors((-1, -1, ''), grid)
        self.assertEqual(len(n), 0)

    def test_find_paths(self):
        grid = [[False for width in range(5)]
                for height in range(5)]
        destinations = pizzabot.get_destination_coords(['1,3', '4,4'])
        paths = pizzabot.find_paths(grid, destinations)
        self.assertEqual(len(paths), 12)
        destinations = pizzabot.get_destination_coords([])
        paths = pizzabot.find_paths(grid, destinations)
        self.assertEqual(len(paths), 0)
        destinations = pizzabot.get_destination_coords(['-1, -1'])
        self.assertEqual(len(paths), 0)

    def test_build_direction_string(self):
        grid = [[False for width in range(5)]
                for height in range(5)]
        destinations = pizzabot.get_destination_coords(['1,3', '4,4'])
        paths = pizzabot.find_paths(grid, destinations)
        pstring = pizzabot.build_direction_string(paths)
        self.assertEqual(pstring, 'ENNNDEEEND')
        self.assertEqual(len(destinations), pstring.count('D'))
        destinations = pizzabot.get_destination_coords(
            ['0, 0', '1, 3', '4, 4', '4, 2', '4, 2', '0, 1', '3, 2', '2, 3', '4, 1'])
        paths = pizzabot.find_paths(grid, destinations)
        pstring = pizzabot.build_direction_string(paths)
        self.assertEqual(pstring, 'DENNNDEEENDSSDDWWWWSDEEENDWNDEESSD')
        self.assertEqual(len(destinations), pstring.count('D'))


if __name__ == '__main__':
    unittest.main()
