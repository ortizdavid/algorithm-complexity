import csv
import pandas
from database.sqlite import SQLite as db

class CsvReading:

    @classmethod
    def read1(cls, file_data):
        file = open(file_data)
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            db.insert(row[0], row[1], row[2], row[3])

    @classmethod
    def read2(cls, file_data):
        df = pandas.read_csv(file_data)
        for i, data in df.iterrows():
            db.insert(data['name'], data['age'], data['gender'], data['created_at'])

    @classmethod
    def read3(cls, file_data):
        with open(file_data, 'r') as file:
            [db.insert(data['name'], data['age'], data['gender'], data['created_at']) for data in csv.DictReader(file)]
        

    @classmethod
    def read4(cls, file_data):
        with open(file_data, 'r') as file:
            data_csv = csv.DictReader(file)
            for data in data_csv:
                db.insert(data['name'], data['age'], data['gender'], data['created_at'])
 
            