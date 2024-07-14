# Import necessary libraries
from Extract import *
import csv
import json
import pymysql
class Load:
    # load class must be able to save the data to the target format
    def to_csv(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("Provide a valid csv file path.")
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
            
    def to_json(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("Provide a valid JSON file path.")
        with open(file_path, 'w') as jsonfile:  
            json.dump(dataset, jsonfile)
            
    def to_mysql(self):
        pass

    def to_postgres(self):
        pass

#### Extract
ex = Extract()
dataset = ex.from_csv(file_path = '<------->/stocks.csv', delimiter = ',') # To be replaced by file path

#### Loading
lo = Load()
lo.from_csv(file_path = '<------->/stocks.csv', dataset = dataset) # To be replaced by file path