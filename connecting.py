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

conn_string = "host="+ stat.postgre_host +" port="+ stat.postgre_port +" dbname="+ stat.postgre_database +" user=" + stat.postgre_user \
+" password="+ stat.postgre_password
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
