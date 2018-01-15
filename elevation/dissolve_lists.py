sample_data = [[969, 3120], [3120, 969], [3154, 3211], [3211, 3154]]

# out_list = []
out_list = [out_list.append(i) for i in [sorted(x) for x in sample_data] if i not in out_list]
print out_list
