from floyd_recursion import floyd, graph_creator
from geeks_floyd import floydWarshall
import time
import sys
from io import StringIO


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
        

def recursion_performance():        
       
    start_time_recur = time.perf_counter()

    for i in range(0,10000):
        graph_size = 4
        graph_param = graph_creator(graph_size)
        with Capturing() as output:
            floyd(graph_param)

    end_time_recur = time.perf_counter()

    execution_time_recur = end_time_recur - start_time_recur
    return execution_time_recur

    
    
def iterative_performance():
    start_time_iter = time.perf_counter()

    for i in range(0,10000):
        graph_size = 4
        graph_param = graph_creator(graph_size)
        with Capturing() as output:
            floydWarshall(graph_param)
    end_time_iter = time.perf_counter()

    execution_time_iter = end_time_iter - start_time_iter
    return execution_time_iter
    
    
def comparision():
    execution_time_recursion = recursion_performance()
    execution_time_itersion = iterative_performance()
    
    print(f"The execution time of recursion (10,000 times) is: {execution_time_recursion}")
    print(f"The execution time of iteration (10,000 times) is: {execution_time_itersion}")
    
    if execution_time_itersion > execution_time_recursion:
        ratio = ( execution_time_recursion / execution_time_itersion - 1 ) * ( -1 )
        ratio = "{0:.0f}%".format(ratio * 100)
        print('Recursion version is about ', ratio, ' faster than iterative version.')
        
    else :
        ratio = ( execution_time_itersion / execution_time_recursion - 1 ) * ( -1 )
        ratio = "{0:.0f}%".format(ratio * 100)
        print('Iterative version is about ', ratio, ' faster than recursion version.')
        
if __name__ == '__main__':
    comparision()