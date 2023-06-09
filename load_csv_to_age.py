"""
Author: Zainab Saad
GitHub: Zainab-Saad
"""
import age, csv
from typing import Tuple

def get_contents_from_csv(file_path) -> Tuple[list, list]:
    """
    Parameters:
    file: path of the csv file

    Returns:
    header[], records [[]]
    """
    # open file 
    file = open(file_path)
    # use csv.reader object to read the csv file
    csvreader = csv.reader(file)
    # extract field names
    header = []
    header = next(csvreader)
    # extract the records
    records = []
    for record in csvreader:
        records.append(record)
    return header, records

def make_map(header: str) -> str:
    """
    Parameters:
    header: names of properties of vertex/edge

    Returns:
    string --> property_name: property_value(%s)
    """
    properties = ''
    for each_property in header:
        properties += each_property + ': %s, '
    return properties[0: len(properties)-2]

def load_labels_from_file(ag: age.age.Age, csv_file_path: str, label_name: str) -> None:
    """"
    Parameters:
    connection object: connection to postgresql using age extension
    file path
    label name
    """
    
    # get property names, property values from csv
    header, records = get_contents_from_csv(csv_file_path)
    # get the properties string to make the vertex/node
    properties = make_map(header)
    for record in records:
        if label_name == '':
            cursor = ag.execCypher('CREATE (n' + '{' + properties + '}) RETURN n', params=tuple(record))
        else:
            cursor = ag.execCypher('CREATE (n: ' + label_name + '{' + properties + '}) RETURN n', params=tuple(record))
    ag.commit()

def load_edges_from_file(ag: age.age.Age, csv_file_path: str, label_name: str) -> None:

    # define an inner function to get the names of all the properties that will be used for matching vertices (in case more than one property is given)
    def get_property_names() -> Tuple[list, list]:
        first_vertex_property_names, second_vertex_property_names, edge_property_names = [], [], []
        v1_index = header.index('start_vertex_type')
        v2_index = header.index('end_vertex_type')
        for i, property_name in enumerate(header):
            if i < v1_index:
                first_vertex_property_names.append(property_name)
            elif (i == v1_index or i == v2_index):
                continue
            elif (i < v2_index):
                second_vertex_property_names.append(property_name)
            else:
                edge_property_names.append(property_name)
        return first_vertex_property_names, second_vertex_property_names, edge_property_names
            
        
    # inner function to get the values of all properties for both vertices
    def get_property_values():
        first_vertex_property_values, second_vertex_property_values, edge_property_values = [], [], []
        for i in range(0, num_first_vertex):
            first_vertex_property_values.append(record[i])
        for i in range(num_first_vertex+1, num_first_vertex+1+num_second_vertex):
            second_vertex_property_values.append(record[i])
        for i in range(num_second_vertex+1, num_second_vertex+1+num_edge):
            edge_property_values.append(record[i])
        return first_vertex_property_values, second_vertex_property_values, edge_property_values

    # get all the edges
    header, records = get_contents_from_csv(csv_file_path)
    # get all the properties for matching each vertex
    first_vertex_property_names, second_vertex_property_names, edge_property_names = get_property_names()
    properties_map_1, properties_map_2, properties_map_3 = make_map(first_vertex_property_names), make_map(second_vertex_property_names), make_map(edge_property_names)
    num_first_vertex, num_second_vertex, num_edge = len(first_vertex_property_names), len(second_vertex_property_names), len(edge_property_names)
    for record in records:
        first_vertex_property_values, second_vertex_property_values, edge_property_values = get_property_values()
        first_vertex_label, second_vertex_label = record[num_first_vertex], record[num_first_vertex+num_second_vertex+1]
        cursor = ag.execCypher('MATCH (u: ' + first_vertex_label + '{' + properties_map_1 + '}), (v: ' + second_vertex_label  + '{' + properties_map_2 +'}) CREATE (u)-[e: ' + label_name + '{' + properties_map_3 + '}' + ']->(v) RETURN e', 
                               params=tuple(first_vertex_property_values)+tuple(second_vertex_property_values)+tuple(edge_property_values)) 
    ag.commit()