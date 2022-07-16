# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from datetime import datetime

moment_time = datetime.today()
random = int(f"{moment_time.month}" + f"{moment_time.day}" + f"{moment_time.second}" + f"{moment_time.microsecond}")%10000*13
print(random)