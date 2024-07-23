import os
from pathlib import Path
from PIL import Image

os.chdir('../')
os.chdir('../')
path = '/dataset/tmp_4' # Здесь определяется в какой папке обрабатываются файлы
print("Текущий рабочий каталог: {0}".format(os.getcwd()))
# В этой же папке должен быть каталог tmp, куда запишутся обработанные файлы

def get_list_of_files(path):
    '''
    функция принимает путь к каталогу и возврашает список файлов с заданным расширением в этом каталоге
    :return: список файлов
    '''
    try:
        os.chdir(path)
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Каталог: {0} не существует".format(path))
    except NotADirectoryError:
        print("{0} не каталог".format(path))
    except PermissionError:
        print("У вас нет прав на изменение {0}".format(path))


    # unsorted_file_list = os.listdir()
    # sorted_file_list = sorted(unsorted_file_list)
    sorted_file_list = os.listdir() #Нам не нужно сортировать список, поэтому сразу так
    list_of_file = []
    for filename in sorted_file_list:
        if os.path.isfile(filename) and Path(filename).suffix == '.jpg':
            list_of_file.append(filename)
    return list_of_file

list_of_files = get_list_of_files(path)
print(list_of_files)

size=(640, 640)
count = 1  # Число с которого надо начать нумерацию
for file in list_of_files:
    count_string = str(count)
    count_string = '0'*(5-len(count_string))+count_string
    new_name = 'tmp\\radiator_'+count_string+'.jpg'
    count += 1
    image = Image.open(file)
    image.thumbnail(size)
    image.save(new_name);
