# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных 
# чисел.

from time import time, time_ns


print(int(time()) % 10)

print(str(time_ns())[-3] + str(time_ns())[-4] +str(time_ns())[-5])



