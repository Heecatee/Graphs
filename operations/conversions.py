def adjacency_list_to_adjacency_matrix(adj_list):
    adjacency_matrix = [None] * len(adj_list)
    for i in range(0, len(adjacency_matrix)):
        edge = [0] * len(adj_list)
        adjacency_matrix[i] = edge
    for row in adj_list:
        vertex_id = int(row[0][:-1])
        i = 1
        while i < len(row):
            connection = row[i]
            if i >= vertex_id:
                adjacency_matrix[vertex_id][connection] = 1
                adjacency_matrix[connection][vertex_id] = 1
            i += 1
    return adjacency_matrix


def adjacency_matrix_to_adjacency_list(matrix):
    adj_list = []
    for i in range(0, len(matrix)):
        adj_list.append([str(i) + ":"])
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list


def adjacency_list_to_incident_matrix(adj_list):
    # incident matrix is prepared in  its transposed form
    incident_matrix = []
    for row in adj_list:
        vertex_id = int(row[0][:-1])
        i = 1
        while i < len(row):
            connection = row[i]
            if connection > vertex_id:
                edge = [0] * len(adj_list)
                edge[vertex_id] = 1
                edge[i] = 1
                incident_matrix.append(edge)
            i += 1
    # transposing matrix
    incident_transposed = [None] * len(incident_matrix[0])
    for i in range(0, len(incident_transposed)):
        edge = [0] * len(incident_matrix)
        incident_transposed[i] = edge
    for i in range(0, len(adj_list)):
        for j in range(0, len(incident_matrix)):
            incident_transposed[i][j] = incident_matrix[j][i]
    return incident_transposed


def adjacency_matrix_to_incident_matrix(matrix):
    incident_matrix = []
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] == 1:
                edge = [0] * len(matrix)
                edge[i] = 1
                edge[j] = 1
                incident_matrix.append(edge)
    # transposing matrix
    incident_transposed = []
    incident_transposed = [None] * len(incident_matrix[0])
    for i in range(0, len(incident_transposed)):
        edge = [0] * len(incident_matrix)
        incident_transposed[i] = edge
    for i in range(0, len(matrix)):
        for j in range(0, len(incident_matrix)):
            incident_transposed[i][j] = incident_matrix[j][i]
    return incident_transposed


def incident_matrix_to_adjacency_list(inc_matrix):
    incident_transposed = [None] * len(inc_matrix[0])
    for i in range(0, len(incident_transposed)):
        edge = [0] * len(inc_matrix)
        incident_transposed[i] = edge
    for i in range(0, len(inc_matrix)):
        for j in range(0, len(inc_matrix[0])):
            incident_transposed[j][i] = inc_matrix[i][j]
    adj_list = []
    for i in range(0, len(inc_matrix)):
        adj_list.append([str(i) + ":"])
    for row in incident_transposed:
        i = 0
        while i < len(row):
            if row[i] == 1:
                j = i + 1
                while row[j] != 1:
                    j += 1
                adj_list[i].append(j)
                adj_list[j].append(i)
                break
            i += 1
    return adj_list


def incident_matrix_to_adjacency_matrix(inc_matrix):
    incident_transposed = [None] * len(inc_matrix[0])
    for i in range(0, len(incident_transposed)):
        edge = [0] * len(inc_matrix)
        incident_transposed[i] = edge
    for i in range(0, len(inc_matrix)):
        for j in range(0, len(inc_matrix[0])):
            incident_transposed[j][i] = inc_matrix[i][j]
    adj_matrix = [None] * len(inc_matrix)
    for row_ind in range(0, len(adj_matrix)):
        edge = [0] * len(adj_matrix)
        adj_matrix[row_ind] = edge
    for row in incident_transposed:
        i = 0
        while i < len(row):
            if row[i] == 1:
                j = i + 1
                while row[j] != 1:
                    j += 1
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1
                break
            i += 1
    return adj_matrix
