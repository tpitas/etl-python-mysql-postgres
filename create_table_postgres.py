#!/usr/bin/env python

import psycopg2
conn = psycopg2.connect("dbname='retail_db' user='postgres' host='localhost' password='Passw0rd'")
with conn.cursor() as cur:
    try:
        cur.execute("""
                    CREATE TABLE cogsley_sales (
                        RowID int4,
                        OrderID int4,
                        OrderDate text,
                        OrderMonthYear text,
                        Quantity int4,
                        Quote int4,
                        DiscountPct float8,
                        Rate int4,
                        SaleAmount float8,
                        CustomerName text,
                        CompanyName text,
                        Sector text,
                        Industry text,
                        City text,
                        ZipCode int4,
                        State text,
                        Region text,
                        ProjectCompleteDate text,
                        DaystoComplete int4,
                        ProductKey text,
                        ProductCategory text,
                        ProductSubCategory text,
                        Consultant text,
                        Manager text,
                        HourlyWage int4,
                        RowCount int4,
                        WageMargin float8
                        );
                    """)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

conn.commit()       
conn.close()
