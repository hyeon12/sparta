a = (1,2,3)
print(a[0]) #1

a = (1,2,3)
# a[0] = 99 이런 작업이 불가능함

a_dict = [('bob','24'),('john','29'),('smith','30')]

a = [1,2,3,4,5,3,4,2,1,2,4,2,3,1,4,1,5,1]
a_set = set(a)
print(a_set)  #{1, 2, 3, 4, 5}

a = set(['사과','감','수박','참외','딸기'])
b = set(['사과','멜론','청포도','토마토','참외'])
print(a & b)  # 교집합
print(a | b)  # 합집합

student_a = set(['물리2','국어','수학1','음악','화학1','화학2','체육'])
student_b = set(['물리1','수학1','미술','화학2','체육'])
print(student_a - student_b)
