"""
Author: Zainab Saad
GitHub: Zainab-Saad
"""
import age, load_csv_to_age as ld

GRAPH_NAME = "csv_load_age"
DSN = "host=127.0.0.1 port=5432 dbname=postgres user=postgres password=12345"
# connect to postgreSQL database using AGE extension
age_obj = age.Age()
ag = age_obj.connect(graph=GRAPH_NAME, dsn= DSN)

# test the function 
ld.load_labels_from_file(ag, './age_load/data/countries.csv', 'Country')
ld.load_labels_from_file(ag, './age_load/data/cities.csv', 'City')
ld.load_edges_from_file(ag, './age_load/data/edges.csv', 'BELONGS_TO')
