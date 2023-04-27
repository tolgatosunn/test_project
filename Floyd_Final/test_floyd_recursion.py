'''
This module performs unit tests of the functions in floyd_recursion module.
'''

import unittest
from unittest.mock import patch
import sys
from io import StringIO
from floyd_recursion import graph_creator, floyd, print_graph, get_user_input


class Capturing(list):
    '''
    This class catches the printed result.
    It will be needed to test whether printed results are valid or not.
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class TestFloydRecursion(unittest.TestCase):
    '''
    This class performs unit tests all the functions in floyd_recursion module.
    '''


    @patch('builtins.input', return_value=5)
    def test_get_user_input(self, mock_input):
        '''
        This function tests the input registered by user is a valid integer or not.
        '''
        result = get_user_input()
        self.assertEqual(result, 5)


    @patch('builtins.input', return_value="This is string!")
    def test_invalid_input_string(self, mock_input):
        '''
        This function tests that if the input registered by user
        is not an integer, the fuction must raise an error and exit the system.
        '''
        with self.assertRaises(SystemExit):
            get_user_input()
            self.assertRaises(ValueError)
            unittest.main(exit=False)


    @patch('builtins.input', return_value=int(-10))
    def test_invalid_input_negative(self, mock_input):
        '''
        Graph size can not be negative.
        Hence, this function tests that if the input registered by user
        is an negative integer, the fuction must raise an error and exit the system.
        '''
        with self.assertRaises(SystemExit):
            get_user_input()
            self.assertRaises(ValueError)
            unittest.main(exit=False)


    def test_graph_size(self):
        '''
        This function tests that if the graph is generated based on the registered
        graph range or not.
        Length of the generated graph must equal to the input graph size.
        Length of the rows of the generated graph must equal to the input graph size.
        '''
        graph_range = 5
        graph = graph_creator(graph_range)
        self.assertEqual(len(graph), graph_range)
        for row in graph:
            self.assertEqual(len(row), graph_range)


    def test_same_nodes_zero_dist(self):
        '''
        The distance between the same nodes must be zero.
        This functions tests the above statement.
        '''
        graph_range = 5
        graph = graph_creator(graph_range)
        for i in range(graph_range):
            self.assertEqual(graph[i][i], 0)


    def test_print_graph(self):
        '''
        The "print_graph" function must print provided graph.
        This function tests whether the "print_graph" function prints correctly.
        To make the comparison more manageable, the printed output of the "print_graph"
        is captured and converted to a string—additionally,
        all the line breakers and blank spaces are removed.
        '''
        distance = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
        expected_output = str('012103230')

        with Capturing() as output:
            print_graph(distance)

        output_str = ''.join(output).replace('\n', '').replace(' ', '')

        self.assertEqual(output_str, expected_output)


    def test_floyd(self):
        '''
        The "floyd" function which is the main function of the module gets a graph
        as an input and finds the shortest distance between the nodes. Then, it generates
        a solution graph with the shortest distances. Lastly, it prints out the solution graph.
        This function tests the printed solution graph is correct or not.
        '''

        graph = [[0, 2, 4, 3], [5, 0, 1, 2], [3, float('inf'), 0, 1], [1, 2, 3, 0]]

        distance = [[0, 2, 3, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0]]

        with Capturing() as output:
            print_graph(distance)

        output_str = ''.join(output).replace('\n', '').replace(' ', '')

        with Capturing() as output_floyd:
            floyd(graph)

        output_str_floyd = ''.join(output_floyd).replace('\n', '').replace(' ', '')

        # Assert that the result is correct
        self.assertEqual(output_str, output_str_floyd)


if __name__ == '__main__':
    unittest.main()
