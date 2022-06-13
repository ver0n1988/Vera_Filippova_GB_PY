import json

from itertools import zip_longest


def get_dict(
        res_path="./res.csv",
        user_path="./users.csv",
        hobby_path="./hobby.csv"):


    user_strs = None
    hobby_strs = None

    with open(user_path, "r", encoding="utf-8") as file_1:
        user_strs = file_1.readlines()

    with open(hobby_path, "r", encoding="utf-8") as file_2:
        hobby_strs = file_2.readlines()

    if len(user_strs) < len(hobby_strs):
        return 1

    my_dict = {}

    for name, hobby in zip_longest(user_strs, hobby_strs):
        name = name.replace("\n", "")
        my_dict[name] = hobby.replace("\n", "") if hobby else None

    with open(res_path, "w+", encoding="utf-8") as res_file:
        json.dump(my_dict, res_file)

    return 0


if __name__ == "__main__":

    exit(get_dict())

