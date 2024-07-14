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
            
    def to_mysql(self, host, username, password, db, table, dataset): # Need MySQL Connection Strings
        # For installation of MySQL follow https://dev.mysql.com/doc/refman/8.4/en/installing.html
        # Database and Table to be created prior of to_mysql method
        # host = "localhost", username = "root", password = "Passw0rd", db = "dbstocks", table = "stocks"
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("Input a valid database name.")
        if not table:
            raise Exception("Input a valid table name")    
        db = pymysql.connect(host = host, user=username, password = password, db = db, 
                        cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table,
                    columns=",".join(row.keys()), values = placeholder)
            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()         

    def to_postgres(self):
        pass

#### Extract
ex = Extract()
dataset = ex.from_csv(file_path = '<------->/stocks.csv', delimiter = ',') # To be replaced by file path

#### Loading
lo = Load()
# lo.from_csv(file_path = '<------->/stocks.csv', dataset = dataset) # To be replaced by file path

lo.to_mysql(host = "localhost", username = "root", password = "Passw0rd", db = "dbstocks", table = "stocks", dataset = dataset)

