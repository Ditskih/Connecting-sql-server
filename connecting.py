# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:20:07 2020

@author: Ditskih
"""

import psycopg2
import os
import numpy as np
import pandas as pd
import connection_stat as stat
import pandas.io.sql as psql
#import sys

conn_string = "host="+ stat.postgrehost +" port="+ "5432" +" dbname="+ stat.postgredatabase +" user=" + stat.postgreuser \
+" password="+ stat.postgrepassword
conn=psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()


def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table)) #you can adjust the query itself here
    print (sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return (data)

jd_do = load_data("schema_name","table_name")
