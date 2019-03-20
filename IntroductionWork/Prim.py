def prim(G, money_one):
    select_point = [0]
    select_path_length = 0
    all_point = len(G)
    remain_point = [x for x in range(1, all_point)]
    for i in range(all_point-1):
        key = float('inf')
        tag = 0
        for j in select_point:
            for k in remain_point:
                if G[j][k] < key:
                    key = G[j][k]
                    tag = k
        select_path_length += key
        select_point.append(tag)
        remain_point.remove(tag)
    return select_path_length * money_one