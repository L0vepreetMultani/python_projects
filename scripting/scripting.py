import os
# operating system
import json
# for working with json files
import shutil
# for copy and rewrite
import sys

YEAR_TO_FIND = '2022'

# creates the new directory to add the selected files to it


def create_new_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_name_from_path(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    return new_names


def copy(source, dest):
    if os.path.exists(dest):
        os.remove(dest)
    shutil.copy(source, dest)


def find_all_students(source):
    student_path = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if YEAR_TO_FIND in file:
                path = os.path.join(source, file)
                student_path.append(path)
        break
    return student_path


def main(source, target):
    cwd = os.getcwd()
    intial_path = os.path.join(cwd, source)
    final_path = os.path.join(cwd, target)

    student_data_path = find_all_students(intial_path)
    new_2022_dirs = get_name_from_path(student_data_path, year)
    create_new_directory(final_path)
    for src, dest in zip(student_data_path, new_2022_dirs):
        dest_path = os.path.join(final_path, dest)
        copy(src, dest_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("you haave to pass a intial and final directory")
year = input(
    "which year files do you want[2021,2022,2023][By defalut year is 2022]")

if (year == '2021' or year == '2022' or year == '2023'):
    YEAR_TO_FIND = year

intial = args[1]
final = args[2]
main(intial, final)
