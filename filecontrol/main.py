from sys import platform
from time import sleep
from os import chdir,mkdir,listdir
import config
from shutil import move


def replase_file(list_file):
    for i in range(len(list_file)):
        file_name = list_file.pop()
        fl_list = file_name.split('.')
        dict_fl = config.dict_sort
        dir_from_sort = dict_fl.get(fl_list[len(fl_list) - 1])

        if dir_from_sort == None:
            dir_to = config.dir_to
        else:
            dir_to = dir_from_sort
        move(f'{config.dir_from}/{file_name}', f'{dir_to}/{file_name}')


if __name__ == '__main__':

    #    print(platform, config.dir_from)
    while True:
        sleep(10)
        for el in config.dict_sort.values():
            try:
                mkdir(el)
            except FileExistsError:
                pass

        chdir(config.dir_from)
        replase_file(listdir())
