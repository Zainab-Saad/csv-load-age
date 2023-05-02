"""
Author: Zainab Saad
GitHub: Zainab-Saad
"""
import age, load_age_to_csv as ld

GRAPH_NAME = "csv_load_age"
DSN = "host=127.0.0.1 port=5432 dbname=postgres user=postgres password=12345"
# connect to postgreSQL database using AGE extension
age_obj = age.Age()
ag = age_obj.connect(graph=GRAPH_NAME, dsn= DSN)

# test the function 
# ld.load_labels_into_file(ag, GRAPH_NAME)
ld.load_edges_into_file(ag, GRAPH_NAME)