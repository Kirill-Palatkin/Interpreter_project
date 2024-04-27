Интерпретатор операций над целочисленными массивами. Приложение оперирует целочисленными массивами произвольной длины с именами из множества {А, В, ..., Z}. Система команд данного интерпретатора (прописные и строчные буквы отождествляются):
• Load A, in.txt; - загрузить в массив А целые числа из файла in.txt (во входном файле могут произвольно присутствовать сепарирующие символы - пробелы, табуляции и переносы строк; также могут быть невалидные строковые репрезентации элементов массива);
• Save A, out.txt; - выгрузить элементы массива А в файл out.txt;
• Rand A, count, Ib, rb; - заполнить массив А псевдослучайными элементами из отрезка [lb; lr] в количестве count штук.
• Concat A, b; - сконкатенировать два массива А и В результат сохранить в массив А;
• Free(a); - очистить массив А и сопоставить переменную А с массивом из 0 элементов;
• Remove a, 2, 7; - удалить из массива а 7 элементов, начиная с элемента с индексом 2;
• Сору А, 4, 10, b; - скопировать из массива А элементы с 4 по 10 (оба конца включительно) и сохранить их в b;
• Sort A+; - отсортировать элементы массива А по неубыванию;
• Sort A-; - отсортировать элементы массива А по невозрастанию;
• Shuffle A; - переставить элементы массива в псевдослучайном порядке;
• Stats a; - вывести в стандартный поток вывода статистическую информацию о массиве
А: размер массива, максимальный и минимальный элемент (и их индексы), наиболее часто встречающийся элемент (если таковых несколько, вывести максимальный из них по значению), среднее значение элементов, максимальное из значений отклонений элементов от среднего значения;
• Print a, 3; - вывести в стандартный поток вывода элемент массива А стоящий на позиции с номером 3;
• Print a, 4, 16; - вывести в стандартный поток вывода элементы массива А, начиная с 4 по 16 включительно оба конца;
• Print a, all; - вывести в стандартный поток вывод все элементы массива А.
Индексирование в массивах начинается с 0. Для сортировки массивов и реализации инструкции
Shuffle используйте алгоритм быстрой сортировки. Предоставьте текстовый файл с инструкциями для реализованного интерпретатора и продемонстрируйте его работу. Обработайте ошибки времени выполнения инструкций.
