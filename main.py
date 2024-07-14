# 1. Написать функцию, 
# которая принимает на вход список целых чисел и возвращает новый список, 
# содержащий только уникальные элементы из исходного списка.
def first_task(int_list:list) -> list:
    return list(set(int_list))


# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
# и возвращает список всех простых чисел в заданном диапазоне.
def second_task(first:int, second:int) -> list:
    return [i for i in range(first,second + 1)]


# 3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
# Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, 
# а также для получения и изменения координат.
class Point:
    
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
        
    def get_distance(point_one:object, point_two:object) -> float:
        return ((point_one.x - point_two.x)**2 + (point_one.y - point_two.y)**2)**0.5
    
    @property
    def coordinates(self) -> tuple:
        return self.x, self.y 
    
    @coordinates.setter
    def coordinates(self, new:tuple) -> bool:
        self.x = new[0]
        self.y = new[1]
        return True


# 4. Написать программу, которая сортирует список строк по длине, 
# сначала по возрастанию, а затем по убыванию.
def fourth_task(strs:list) -> tuple:
    asc_sort = sorted(strs, key=len) 
    desc_sort = sorted(strs, key=len, reverse=True) 
    return asc_sort, desc_sort






# TEST CASES # TEST CASES # TEST CASES 
# TEST CASES # TEST CASES # TEST CASES 
# TEST CASES # TEST CASES # TEST CASES 
if __name__ == "__main__":
    # 1 task test
    print(f"[1] - {first_task([1,2,2,3,45,6,7,1,1,1,1,1,-1,-100000,-100000,-100000])}")
    
    
    # 2 task test
    print(f"[2] - {second_task(-5,10)}")
    
    
    # 3 task test
    p1 = Point(1,6.123213)
    p2 = Point(-10,8.123213)
    
        # get_distance
    print(f"Расстояние от p1 до p2 = {Point.get_distance(p1, p2)}")
    
        # coordinate getter setter
    print(f"Координаты p1 getter - {p1.coordinates}")
    p1.coordinates = -11, 220
    print("Координаты p1 setter - True")
    print(f"Координаты p1 getter - {p1.coordinates}")
    
    
    # 4 task test
    print(f'[4] - {fourth_task(["Змея", "Python", "Северная Дакота", "Хочу", "Работать", ":)"])}')