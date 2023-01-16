"""
To read text file columns
"""
from pathlib import Path
import re, pandas

file = Path(r"C:\Users\matth\Documents\School\University\Delft\Courses\Year 2\Q2\Aero II\High Speed Practical\testfile.txt")

# for test_results
def x_y_extract(filepath):
    new_data = list(filter(None, [re.split('\s+', i.strip('\n')) for i in open(filepath)]))
    # result = pandas.DataFrame(new_data)

    x = []
    y = []
    for row in new_data:
        x.append(float(row[1]))
        y.append(float(row[2]))

    return x,y

x,y = x_y_extract(file)
print(x,y)






# # for channel variation file
# def x_y_extract_channel(filepath):
#     new_data = list(filter(None, [re.split('\s+', i.strip('\n')) for i in open(filepath)]))
#     # result = pandas.DataFrame(new_data)

#     x_dist = []
#     y_dist = []
#     A_dist_ratio = []
#     for row in new_data:
#         x_dist.append(float(row[0]))
#         y_dist.append(float(row[1]))
#         A_dist_ratio.append(float(row[2]))


#     return x_dist, y_dist, A_dist_ratio

# x_dist, y_dist, A_dist_ratio = x_y_extract_channel(file)
# print(x_dist, y_dist, A_dist_ratio)







# for adjustable diffuser variation file
# def x_y_extract_channel(filepath):
#     new_data = list(filter(None, [re.split('\s+', i.strip('\n')) for i in open(filepath)]))
#     # result = pandas.DataFrame(new_data)

#     x_dist = []
#     y_dist = []
#     A_dist_ratio = []
#     for row in new_data:
#         x_dist.append(float(row[0]))
#         y_dist.append(float(row[1]))
#         A_dist_ratio.append(float(row[2]))


#     return x_dist, y_dist, A_dist_ratio

# x_dist, y_dist, A_dist_ratio = x_y_extract_channel(file)
# print(x_dist, y_dist, A_dist_ratio)