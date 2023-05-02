import age, csv, copy

# TODO -- refactor code so that file is not open again and again inside the loop 
def load_labels_into_file(ag: age.age.Age,  graph_name: str) -> None:
    """
    Paramters:
    Age class object
    graph name
    """

    cursor = ag.execCypher('MATCH (u) RETURN u')
    # create a seperate csv file for each label and write the properties header, records there
    cursor_fetch = cursor.fetchall()
    label , file_path = '', ''
    for i,row in enumerate(cursor_fetch):
        file_path = './age_load/data/' + label + '.csv'
        row_label = list(cursor_fetch)[i][0].label
        if(row_label != label):
            label = row_label
            file_path = './age_load/data/' + label + '.csv'
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(list((row[0].properties).keys()))
                writer.writerow(list((row[0].properties).values()))
        else:
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(list((row[0].properties).values()))

    
def load_edges_into_file(ag: age.age.Age, graph_name: str) -> None:
    cursor = ag.execCypher('MATCH p = ()-[]->() RETURN p')
    # create a seperate csv file for each label and write the properties header, records there
    cursor_fetch = cursor.fetchall()
    label , file_path = '', ''
    for i,row in enumerate(cursor_fetch):
        file_path = './age_load/data/' + label + '.csv'
        row_label = row[0][1].label
        header = list(row[0][0].properties.keys()) + ['start_vertex_type'] + list(row[0][2].properties.keys()) + ['end_vertex_type']
        record =  list(row[0][0].properties.values()) + [row[0][0].label, ] + list(row[0][2].properties.values()) + [row[0][2].label, ] 
        print(header)
        print(record)
        if(row_label != label):
            label = row_label
            file_path = './age_load/data/' + label + '.csv'
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerow(record)
        else:
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(record)