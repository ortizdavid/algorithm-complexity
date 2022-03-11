from src.timing import Timing as tm
from src.list_sums import ListSum as ls


List = ls.generate_list(60000)
print(List)
print('-----------------------------------------------------------')
tm.calculate_time(ls.sum1, List)
tm.calculate_time(ls.sum2, List)
tm.calculate_time(ls.sum3, List)
tm.calculate_time(ls.sum4, List)
tm.print_time()
print('-----------------------------------------------------------')
tm.faster_alg()
tm.slower_alg()