import csv

def read_csv(csv_path):
    with open(csv_path, 'rb') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        return data_list

def total_climb(data):
    tc = 0
    elv_prv = None
    for elv_cur in [float(i[1]) for i in data]:
        if elv_prv:
            if elv_cur > elv_prv:
                tc += elv_cur - elv_prv
            elv_prv = elv_cur
        else:
            elv_prv = elv_cur
    return int(tc)

def maximum_climb(data):
    mc = 0
    c_list = []
    temp_c = []
    c_start = None
    elv_prv = None
    for elv_cur in [float(i[1]) for i in data]:
        if elv_prv:
            if elv_cur > elv_prv:
                if not c_start:
                    c_start = elv_prv
                    temp_c.append(c_start)
                else:
                    temp_c.append(elv_cur)
            else:
                if len(temp_c) > 1:
                    c_list.append(temp_c)
                c_start = None
                temp_c = []
            elv_prv = elv_cur
        else:
            elv_prv = elv_cur
    mc = max([(i[-1]-i[0]) for i in c_list])
    return int(mc)

def lowest_point(data):
    return int(min([float(i[1]) for i in data]))

def highest_point(data):
    return int(max([float(i[1]) for i in data]))

def course_metrics(csv_path,laps=None):
    data = read_csv(csv_path)
    if laps:
        tc = total_climb(data)*laps
    else:
        tc = total_climb(data)
    print 'TC',tc
    print 'MC',maximum_climb(data)
    print 'HP',highest_point(data)
    print 'LP',lowest_point(data)
    print 'HD',highest_point(data)-lowest_point(data)

course_metrics(r"C:\Users\Sam\Documents\Marshall\elevation\sprint_elevation.csv")
