import os

project_dir = {
    'my_project': [
        {
            'settings': [{'bar': [], 'foo':[]}],
            'mainapp': [],
            'adminapp': [],
            'authapp': []
        }]
}


def script_starter(path, tree):

    for folder, c in tree.items():

        new_path = os.path.join(path, folder)

        if not os.path.exists(new_path):
            os.mkdir(new_path)

        if len(c) > 0:
            for i in c:
                script_starter(new_path, i)


if __name__ == "__main__":

    script_starter(os.getcwd(), tree=project_dir)