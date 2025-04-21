# file = None
#
# try:
#     file = open("scores.txt")
#     contents = file.read()
#     print(contents)
# except OSError:
#     print("File not found")
# finally:
#     file.close() if file else print("File was never opened")


# file = open("scores.txt")
# lines = file.readlines()
# file.close()
#
# for line in lines:
#     print(line.strip())

# out = open("output.txt", "w")
# out.write("Hello World \n")
# out.write("How are you?")
# out.close()

# with open("scores.txt", 'r+') as file:
#     for line in file.readlines():
#         total = 0
#         for item in line.strip().split():
#             total += int(item)
#         file.write(f'\n{total}')

# import os
# my_file = open('hello.txt', 'r')
# file_info = os.stat('hello.txt')
# os.remove('hello.txt')

# import os
# path = os.path.join('dir')
#
# for dir_name, sub_dirs, files in os.walk(path):
#     print(dir_name, 'contains subdirectories:', sub_dirs, end=' ')
#     print('and the files:', files)

import matplotlib.pyplot as plt

with open('math_scores_fl.txt') as my_file:
    math_scores = []
    for t in my_file:
        math_scores.append(float(t))

with open('verbal_scores_fl.txt') as my_file:
    verbal_scores = []
    for t in my_file:
        verbal_scores.append(float(t))

years = range(2005,2016)
plt.plot(years, math_scores, 'ro-', linewidth=1, markersize=3, label='Math scores')
plt.plot(years, verbal_scores, 'bx-', linewidth=1, markersize=3, label='Verbal scores')
plt.legend(shadow=True, loc='right')
plt.xlabel('Year')
plt.ylabel('Score')
plt.title('Florida SAT Scores')
plt.show()
















