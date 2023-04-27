#!/usr/bin/env python
# coding: utf-8

'''
This piece of code first creates a graph with randomly chosen variables
based on the input graph size.
Later, it finds the shortest path between the nodes in the graph.
Lastly, it prints out the input graph and the solution graph,
which includes the shortest distances.
'''

import sys
import random
# This library will be needed to create a graph by random variables.

NO_PATH = 999999
        # NO_PATH defines that If there is no way from one node to another
        # It will be set as NO_PATH and 999999 interger value

def get_user_input():
    '''
    Input: is a range of a graph to be registered by the user.

    Process: This function gets input from the user and checks whether
    it is validated or not.

    Output: is a range of a graph.
    '''

    while True:
        # Input graph_range will be used to produce a graph.
        graph_range = input('''
                Please, input an integer as the size of the graph 
                    to generate it with random values: ''')

        # We try to convert graph_range into an integer.
        # If we get an error which means graph_range is not an integer.
        # Then, it raises a ValueError and exits the system.
        # If the conversion into integer works,
        # the 'if' clause checks whether GRAPH_RANGE is a minus.
        # If yes, it exits the system. If no, it returns graph_range.
        try:
            graph_range = int(graph_range)
        except ValueError:
            print('''
            -----------------------------------------------   
                Graph range must be an integer value.
            ''')
            sys.exit()
        if graph_range < 0:
            print('''
            -----------------------------------------------   
                Graph range can not be negative integer.
            ''')
            sys.exit()

        return graph_range


def graph_creator(graph_size):
    '''
    This function creates a graph with random values.

    Input: Range of a graph.

    Process: A graph is to be created with random variables and
    a size arranged based on the input "size" value.
    For instance, size=4 creates a 4x4 graph.

    Output: A graph.
    '''

    graph = []

    values = [NO_PATH]+list(range(1, 10))
    # We will chose our values for the graph from the values list.

    for i in range(graph_size):  # Loop for the rows
        columns = []
        for j in range(graph_size):  # Loop for the columns
            if i == j:  # Distance should be 0 between same nodes.
                random_value = 0
            else:
                random_value = random.choice(values)
            columns.append(random_value)  # Appending randomly chosen values
        graph.append(columns)  # Appending the row into the graph

    return graph


def floyd(distance, intermediate_node=0):
    """
    This function is a recursion implementation of Floyd's algorithm.

    Input: "distance" is a graph produced by the "graph_creator" function.
            "intermediate_node" is 0 by default.

    Process: The function finds the shortest distance between nodes
    and prints it.

    Output: is printed distance graph.

    """

    start_nodes = end_nodes = list(range(len(distance[0])))
    graph_range = len(distance[0])

    if intermediate_node < graph_range:
        # The function is to be run until "intermediate_node"
        # reaches the graph_range

        for start_node in start_nodes:
            for end_node in end_nodes:
                # The iteration will be proceeded for each "start_node"
                # in "start_nodes" and each "end_node" in "end_nodes"

                if distance[start_node][end_node] >\
                        distance[start_node][intermediate_node]\
                        + distance[intermediate_node][end_node]:
                    # if current distance from start node to end node
                    # is longer than the distance through an intermediate node.
                    # The distance will be updated with the distance
                    # through an intermediate node.

                    distance[start_node][end_node] =\
                            distance[start_node][intermediate_node] \
                            + distance[intermediate_node][end_node]

        # Until intermediate_node reaches the graph_size, floyd function
        # will be run by increasing intermediate_node by 1.
        # And, also updated distance graph will be use as the input.
        return floyd(distance, intermediate_node + 1)

    # When intermediate_node reaches the graph_size, distance graph
    # will be printed by printSolution function.
    print_graph(distance)
    return None


# A utility function to print the solution and the input graphes
def print_graph(distance):
    '''
    This function is to print the input graph or the solution graph produced in floyd
    function.

    Also, it will be used to print the input graph.

    Input: is a graph.

    Process: is printing the distances between each nodes.

    Output: is a print of the graph.
    '''

    graph_size = len(distance[0])
    no_path = 999999

    for i in range(graph_size):  # Loops for rows.
        for j in range(graph_size):  # Loops for columns.

            # If the distance from i to j is equal to no_path
            # which is int(999999), then print "no_path".
            # Else, print the distance itself.
            if distance[i][j] == no_path:
                print(f'{"NO_PATH":>8}', end=' ')
            else:
                print(f'{distance[i][j]:>8}', end=' ')

            # If j reaches (graph_size-1), the function prints
            # to break the line. So, it will continue printing
            # from the next row.
            if j == graph_size-1:
                print('')


if __name__ == '__main__':

    GRAPH_RANGE = get_user_input()
    graph_param = graph_creator(GRAPH_RANGE)

    print('------------------------------------------------------')

    print('''
        Following graph is created by random values
       to be used as the input of the floyd function
            ''')
    print_graph(graph_param)

    print('------------------------------------------------------')

    print('''
        Following graph shows the shortest distances
            between every pair of vertices
        ''')
    # Function call
    floyd(graph_param)
