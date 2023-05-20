"""
Author: Zainab Saad
GitHub: Zainab-Saad
"""

import age, csv, copy

# TODO -- refactor code so that file is not open again and again inside the loop 
def load_labels_into_file(ag: age.age.Age,  graph_name: str) -> None:
    """
    Paramters:
    Age class object
    graph name
    """
    cursor = ag.execCypher('MATCH (u) RETURN DISTINCT labels(u)[0]')
    
    for row in cursor:
        file_path = './age_load/data/' + row[0] + '.csv'
        cursor_vertices = ag.execCypher('MATCH (u:' + row[0] + ') RETURN u')
        cursor_fetch = cursor_vertices.fetchall()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(list((cursor_fetch[0][0].properties).keys()))
            for each_vertex in cursor_fetch:
                writer = csv.writer(file)
                writer.writerow(list((each_vertex[0].properties).values()))
        file.close()

    
def load_edges_into_file(ag: age.age.Age, graph_name: str) -> None:
    
    cursor = ag.execCypher('MATCH (u)-[e]->(v) RETURN DISTINCT type(e)')

    for row in cursor:
        file_path = './age_load/data/' + row[0] + '.csv'
        cursor_edges = ag.execCypher('MATCH p = (u)-[e:' + row[0] + ']->(v) RETURN p')
        cursor_fetch = cursor_edges.fetchall()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = list(cursor_fetch[0][0][0].properties.keys()) + ['start_vertex_type'] + list(cursor_fetch[0][0][2].properties.keys()) + ['end_vertex_type'] + list(cursor_fetch[0][0][1].properties.keys())
            writer.writerow(header)
            for each_edge in cursor_fetch:
                writer = csv.writer(file)
                record =  list(each_edge[0][0].properties.values()) + [each_edge[0][0].label, ] + list(each_edge[0][2].properties.values()) + [each_edge[0][2].label, ] + list(each_edge[0][1].properties.values())
                writer.writerow(record)
        file.close()
