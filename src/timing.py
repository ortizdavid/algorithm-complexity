import time 

class Timing:

    arr_algos = []
    arr_times = []

    @classmethod
    def calculate_time(cls, func, args):
        start = time.time()
        func(args)
        end = time.time()
        total_time = end - start 
        cls.arr_algos.append(func.__name__)
        cls.arr_times.append(total_time)
        return total_time

    @classmethod
    def print_time(cls):
        for i in range(len(cls.arr_algos)):
            print(f'Using {cls.arr_algos[i]}, Time: {cls.arr_times[i]} s')
    
    @classmethod
    def faster_alg(cls):
        shorter = cls.arr_times[0]
        faster = cls.arr_algos[0]
        for i in range(len(cls.arr_times)):
            exec_time = cls.arr_times[i]
            if shorter > exec_time:
                shorter = exec_time
                faster = cls.arr_algos[i]
        print(f'Faster Algorithm: {faster}, Time: {shorter} s')

    @classmethod
    def slower_alg(cls):
        longer = cls.arr_times[0]
        slower = cls.arr_algos[0]
        for i in range(len(cls.arr_times)):
            exec_time = cls.arr_times[i]
            if longer < exec_time:
                longer = exec_time
                slower = cls.arr_algos[i]
        print(f'Slower Algorithm: {slower}, Time: {longer} s')

    
