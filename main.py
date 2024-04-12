# 1. Написать функцию, 
# которая принимает на вход список целых чисел и возвращает новый список, 
# содержащий только уникальные элементы из исходного списка.
def first_task(int_list:list) -> list:
    return list(set(int_list))

print(f"[1] - {first_task([1,2,2,3,45,6,7,1,1,1,1,1,-1,-100000,-100000,-100000])}")


# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
# и возвращает список всех простых чисел в заданном диапазоне.
def second_tast(first:int, second:int) -> list:
    result = []
    for i in range(first,second + 1):
        result.append(i)
    return result

print(f"[2] - {second_tast(-5,10)}")









