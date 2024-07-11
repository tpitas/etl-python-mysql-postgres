# load necessary libraries
import csv
import json
import pymysql
import psycopg2

class Extract:
    def from_csv(self, file_path, delimiter = ",", quotechar = ","):
        if not file_path:
            raise Exception("Please provide a valid file path")

        dataset = []
        with open(file_path) as file: 
            csv_file = csv.DictReader(file, delimiter = delimiter,quotechar = quotechar) 
            for row in csv_file:
                dataset.append(row)
        return dataset

    def from_json(self, file_path):
        if not file_path:
            raise Exception("Please provide a valid file path")
        with open(file_path) as json_file:    
            dataset = json.load(json_file)
        return dataset
    
    def from_mysql(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please provide a valid host, \
            username, password, database, and query.")
        
        db = pymysql.connect(host = host, user = username, password = password, 
                db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        for row in cur:
            dataset.append(row)
        db.commit()
        cur.close()
        db.close()
        return dataset
 
    # def from_postgres(self):
    #     pass
    
ex = Extract()
dataset = ex.from_csv(file_path="<--------->.csv") ## to be replaced
for row in dataset:
    print(row)