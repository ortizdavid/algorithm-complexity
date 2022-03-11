from src.csv_reading import CsvReading as cr
from database.sqlite import SQLite as db
from src.timing import Timing as tm


fname = "files/customers.csv"
db.create_table()
print('-----------------------------------------------------------')
tm.calculate_time(cr.read1, fname)
tm.calculate_time(cr.read2, fname)
tm.calculate_time(cr.read3, fname)
tm.print_time()
print('-----------------------------------------------------------')
tm.faster_alg()
tm.slower_alg()