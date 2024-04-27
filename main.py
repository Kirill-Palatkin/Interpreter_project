import re
import random
from collections import Counter


class Interpreter:

    def __init__(self, array):
        self.name = array
        self.array = []

    def load(self, text_file):
        with open(text_file, 'r', encoding='utf-8') as input_file:
            self.array = re.findall(r'-?\d+', input_file.read())
            self.array = [int(num) for num in self.array]
        print(f'\nСоздан массив {self.name}: {self.array}')

        return self.array, self.name

    def save(self, text_file, arr):
        with open(text_file, 'a', encoding='utf-8') as output_file:
            output_file.write(f'Элементы массива {arr[1]}: ')
            output_file.write(str(arr[0]) + '\n')
        print(f'\nЭлементы массива {arr[1]} выгружены в файл out.txt')

    def rand(self, arr, count, lb, rb):
        arr[0].clear()
        for _ in range(int(count)):
            arr[0].append(random.randint(int(lb), int(rb)))
        print(f'\nМассив {arr[1]} псевдослучайных элементов:', arr[0])

    def concat(self, tuple_1, tuple_2):
        arr_1 = tuple_1[0]
        arr_2 = tuple_2[0]
        arr_1 += arr_2
        print(f'\nКонкатенация массивов {tuple_1[1]} и {tuple_2[1]}: {arr_1}')

    def free(self, array):
        array[0].clear()
        print(f'\nОчищенный массив {array[1]}: {array[0]}')

    def remove(self, arr, start_index, count):
        if start_index < 0 or start_index > len(arr[0]) - 1:
            print(f'\nВ массиве {arr[1]} не существует элемента с индексом {start_index}')
            return False
        if count > len(arr[0]):
            print(f'\nНевозможно удалить {count} элементов в массиве длиной {len(arr)}')
            return False
        del arr[0][start_index:count + start_index]
        print(
            f'\nВ массиве {arr[1]} удалено {count} элемента(ов), начиная с элемента с индексом {start_index}: {arr[0]}')

    def copy(self, tuple_1, start, finish, tuple_2):
        arr_1 = tuple_1[0]
        arr_2 = tuple_2[0]

        if start < 0 or start > len(arr_1):
            print(f'В массиве {tuple_1[1]} не существует {start}-го элемента')
            return False
        if finish > len(arr_1):
            print(f'В массиве {tuple_1[1]} не существует {finish}-го элемента')
            return False

        arr_2.clear()
        arr_2 += arr_1[start - 1:finish]
        print(f'\nИз массива {tuple_1[1]} скопированы значения с {start} по {finish} и сохранены в {tuple_2[1]}')
        print(f'Массив {tuple_2[1]}: {arr_2}')

    def sort(self, arr, sign):
        if sign == '+':
            arr[0].sort()
            print(f'\nМассив {arr[1]} отсортирован в порядке неубывания: {arr[0]}')
        elif sign == '-':
            arr[0].sort(reverse=True)
            print(f'\nМассив {arr[1]} отсортирован в порядке невозрастания: {arr[0]}')

    def shuffle(self, arr):
        random.shuffle(arr[0])
        print(f'\nЭлементы массива {arr[1]} перемешаны в псевдослучайном порядке: {arr[0]}')

    def stats(self, arr):
        counter = Counter(arr[0])
        most_common = counter.most_common()
        max_elem = 0
        max_count = 0

        for elem, count in most_common:
            if max_elem < elem and max_count <= count:
                max_elem = elem
                max_count = count

        deviations = [round(abs(num - sum(arr[0]) / len(arr[0])), 1) for num in arr[0]]
        max_deviation = max(deviations)

        print(f'\n----- Информация о массиве {arr[1]}: -----\n'
              f'Размер: {len(arr[0])}\n'
              f'Максимальный элемент: {max(arr[0])}, его индекс: {arr[0].index(max(arr[0]))}\n'
              f'Минимальный элемент: {min(arr[0])}, его индекс: {arr[0].index(min(arr[0]))}\n'
              f'Максимальный элемент из наиболее часто встречающихся: {max_elem}\n'
              f'Среднее значение элементов: {round(sum(arr[0]) / len(arr[0]), 1)}\n'
              f'Максимальное из значений отклонений элементов от среднего значения: {max_deviation}'
              )

    def print(self, arr, start, finish=None):
        if start.isdigit():
            if int(start) > len(arr[0]):
                print(f'\nВ массиве {arr[1]} не существует {start}-го элемента')
                return False
            if finish is None:
                print(f'\nЭлемент массива {arr[1]}, стоящий на позиции {start}: {arr[0][int(start) - 1]}')
                return True
            elif finish is not None:
                if finish.isdigit():
                    if int(finish) > len(arr[0]):
                        print(f'\nВ массиве {arr[1]} не существует {finish}-го элемента')
                        return False
                    print(f'\nЭлементы массива {arr[1]} с {start} по {finish}: {arr[0][int(start) - 1:int(finish)]}')
                    return True
        else:
            print(f'\nВсе элементы массива {arr[1]}: {arr[0]}')


valid_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

returned_values = []

while True:
    user_input = input('\n\t\t\t\tВыберете опцию из списка (для выхода введите "quit"): \n'
                       '\n• Load имя_массива, in.txt (Имена массивов из множества {A, B,..., Z}) (Пример: Load A, in.txt)'
                       '\n• Save имя_массива, out.txt (Пример: Save A, out.txt)'
                       '\n• Rand имя_массива, кол-во_элементов(число), левая_граница(число), правая_граница(число) (Пример: Rand A, 3, 1, 10)'
                       '\n• Concat имя_массива_1, имя_массива_2 (Пример: Concat A, b)'
                       '\n• Free(имя_массива) (Пример: Free(a))'
                       '\n• Remove имя_массива, индекс_начала_удаления, кол-во_удаляемых_элементов (Пример: Remove a, 2, 7)'
                       '\n• Copy имя_массива_1, позиция_начального_элемента, позиция_конечного_элемента, имя_массива_2 (Пример: Copy A, 4, 10, b)'
                       '\n• Sort имя_массива+/- (+ по возрастанию, - по убыванию) (Пример: Sort A+)'
                       '\n• Shuffle имя_массива (Пример: Shuffle A)'
                       '\n• Stats имя_массива (Пример: Stats a)'
                       '\n• Print имя_массива, позиция_элемента (Пример: Print a, 3)'
                       '\n• Print имя_массива, индекс_начала, индекс_конца (Пример: Print a, 4, 16)'
                       '\n• Print имя_массива, all (Пример: Print a, all)'
                       '\n\nВвод: ')
    normal_split = [item.replace(',', '') for item in user_input.split()]

    if len(normal_split) < 2:
        if (len(user_input) == 7 and user_input.startswith('Free(') and user_input[5].upper() in valid_names
                and user_input.endswith(')')):
            for arr_name in returned_values:
                if user_input[5].upper() == arr_name[1].upper():
                    instance = Interpreter(arr_name)
                    instance.free(arr_name)
                    break
            else:
                print(f'\nМассива {user_input[5].upper()} не существует')
        elif user_input == 'quit':
            break
        else:
            print('\n-----Ошибка-----')

    elif (normal_split[0] == 'Load' and normal_split[1].upper() in valid_names and user_input.split()[0].count(',') == 0
          and user_input.split()[1].count(',') == 1 and user_input.split()[2].count(',') == 0
          and normal_split[2] == 'in.txt'):
        if len(returned_values) == 0:
            instance = Interpreter(normal_split[1].upper())
            result = instance.load(normal_split[2])
            returned_values.append(result)
        for elem in returned_values:
            if normal_split[1].upper() != elem[1]:
                instance = Interpreter(normal_split[1].upper())
                result = instance.load(normal_split[2])
                returned_values.append(result)
                break

    elif (normal_split[0] == 'Save' and normal_split[1].upper() in valid_names and user_input.split()[0].count(',') == 0
          and user_input.split()[1].count(',') == 1 and user_input.split()[2].count(',') == 0
          and normal_split[2] == 'out.txt'):
        for arr_name in returned_values:
            if normal_split[1].upper() == arr_name[1].upper():
                instance = Interpreter(arr_name)
                instance.save(normal_split[2], arr_name)
                break
        else:
            print(f'\nМассива {normal_split[1].upper()} не существует')

    elif (normal_split[0] == 'Rand' and normal_split[1].upper() in valid_names and user_input.split()[2].count(',') == 1
          and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 1
          and user_input.split()[3].count(',') == 1
          and user_input.split()[4].count(',') == 0
          and normal_split[2].isdigit() and int(normal_split[2]) >= 0 and user_input.split()[3].count(',') == 1
          and normal_split[3].isdigit() and user_input.split()[4].count(',') == 0 and normal_split[4].isdigit()
          and int(normal_split[3]) < int(normal_split[4])):
        for arr_name in returned_values:
            if normal_split[1].upper() == arr_name[1]:
                instance = Interpreter(normal_split[1].upper())
                instance.rand(arr_name, normal_split[2], normal_split[3], normal_split[4])
                break
        else:
            print(f'\nМассива {normal_split[1].upper()} не существует')

    elif (normal_split[0] == 'Concat' and normal_split[1].upper() in valid_names
          and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 1
          and user_input.split()[2].count(',') == 0
          and normal_split[2].upper() in valid_names):
        count = 0
        first_arr = ''
        second_arr = ''
        for arr_name in returned_values:
            if normal_split[1].upper() == arr_name[1]:
                count += 1
                first_arr = arr_name
            if normal_split[2].upper() == arr_name[1]:
                count += 1
                second_arr = arr_name
            if count == 2:
                instance = Interpreter(normal_split[1].upper())
                instance.concat(first_arr, second_arr)
                break
        else:
            print(f'\nМассивов {normal_split[1].upper()} или {normal_split[2].upper()} не существует')

    elif (normal_split[0] == 'Remove' and normal_split[1].upper() in valid_names
          and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 1
          and user_input.split()[2].count(',') == 1 and user_input.split()[3].count(',') == 0
          and normal_split[2].isdigit() and int(normal_split[2]) >= 0
          and normal_split[3].isdigit() and int(normal_split[3]) >= 0):
        for arr_name in returned_values:
            if normal_split[1].upper() == arr_name[1].upper():
                instance = Interpreter(arr_name)
                instance.remove(arr_name, int(normal_split[2]), int(normal_split[3]))
                break
        else:
            print(f'\nМассива {normal_split[1].upper()} не существует')

    elif (normal_split[0] == 'Copy' and normal_split[1].upper() in valid_names and user_input.split()[0].count(',') == 0
          and user_input.split()[1].count(',') == 1 and user_input.split()[2].count(',') == 1
          and user_input.split()[3].count(',') == 1 and user_input.split()[4].count(',') == 0
          and normal_split[2].isdigit() and int(normal_split[2]) > 0 and normal_split[3].isdigit()
          and int(normal_split[3]) > 0 and normal_split[4].upper() in valid_names
          and normal_split[1].upper() != normal_split[4].upper()):
        count = 0
        first_arr = ''
        second_arr = ''
        for arr_name in returned_values:
            if normal_split[1].upper() == arr_name[1]:
                count += 1
                first_arr = arr_name
            if normal_split[4].upper() == arr_name[1]:
                count += 1
                second_arr = arr_name
            if count == 2:
                instance = Interpreter(normal_split[1].upper())
                instance.copy(first_arr, int(normal_split[2]), int(normal_split[3]), second_arr)
                break
        else:
            print(f'\nМассивов {normal_split[1].upper()} или {normal_split[4].upper()} не существует')

    elif (normal_split[0] == 'Sort' and len(normal_split[1]) == 2 and normal_split[1][0].upper() in valid_names
            and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 0
            and normal_split[1].endswith('+') or normal_split[1].endswith('-')):
        for arr_name in returned_values:
            if arr_name[1] == normal_split[1][0].upper():
                instance = Interpreter(normal_split[1][0].upper())
                instance.sort(arr_name, normal_split[1][1])
                break
        else:
            print(f'\nМассива {normal_split[1][0].upper()} не существует')

    elif (normal_split[0] == 'Shuffle' and len(normal_split[1]) == 1 and normal_split[1].upper() in valid_names
          and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 0):
        for arr_name in returned_values:
            if arr_name[1] == normal_split[1].upper():
                instance = Interpreter(normal_split[1][0].upper())
                instance.shuffle(arr_name)
                break
        else:
            print(f'\nМассива {normal_split[1].upper()} не существует')

    elif (normal_split[0] == 'Stats' and len(normal_split[1]) == 1 and normal_split[1].upper() in valid_names
            and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 0):
        for arr_name in returned_values:
            if arr_name[1] == normal_split[1].upper():
                instance = Interpreter(normal_split[1][0].upper())
                instance.stats(arr_name)
                break
        else:
            print(f'\nМассива {normal_split[1].upper()} не существует')

    elif normal_split[0] == 'Print':
        if (len(normal_split[1]) == 1 and len(normal_split) == 3 and normal_split[1].upper() in valid_names
                and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 1
                and user_input.split()[2].count(',') == 0
                and (normal_split[2].isdigit() or normal_split[2] == 'all')):
            for arr_name in returned_values:
                if arr_name[1] == normal_split[1].upper():
                    instance = Interpreter(normal_split[1][0].upper())
                    instance.print(arr_name, normal_split[2])
                    break
            else:
                print(f'\nМассива {normal_split[1].upper()} не существует')
        elif (len(normal_split[1]) == 1 and normal_split[1].upper() in valid_names
                and user_input.split()[0].count(',') == 0 and user_input.split()[1].count(',') == 1
                and user_input.split()[2].count(',') == 1 and user_input.split()[3].count(',') == 0
                and normal_split[2].isdigit() and normal_split[3].isdigit()):
            for arr_name in returned_values:
                if arr_name[1] == normal_split[1].upper():
                    instance = Interpreter(normal_split[1][0].upper())
                    instance.print(arr_name, normal_split[2], normal_split[3])
                    break
            else:
                print(f'\nМассива {normal_split[1].upper()} не существует')
        else:
            print('\n-----Ошибка-----')
    else:
        print('\n-----Ошибка-----')