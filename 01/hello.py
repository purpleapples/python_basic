# numbers = set(range(1,10) )
# odds = set(range(1,10,2))
#
# print(numbers, "는", odds, "의 모집합?", numbers.issuperset(odds))
# print(odds, "는", numbers, "의 부분집합?", odds.issubset(numbers))
#
# # zip 의 내부 데이터는 출력될때 pop 된다.
# x = range(1, 8)
# y = range(1, 8)
# z = zip(x,y)
# print(z)
# for i in z:
#     print(i)
#     break
#
# print(z)
#
#
# for i in z:
#     print(i)

#import IPython.nbformat as ipyformat
import os

# conv = convert.read(open('source.py', 'r'), 'txt')
# convert.write(conv, open('source.ipynb', 'w'), 'ipynb')

# for root, subdirs, files in os.walk("D:/data_science/resources/atom_docs/coursera_machineLearning/"):
#     for file in files:
#         with open(root + '/' + file, 'r', encoding='utf8') as f:
#             with open(root+ '/' + file.replace('.txt', '.py'), 'w', encoding='utf8') as fn:
#                 fn.write(f.read())

class Point :
    x = 1
    class Inner_Point:
        y = 2

