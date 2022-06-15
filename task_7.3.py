if __name__ == "__main__":

    import os
    import sys
    import shutil

    main_path = sys.argv[1]
    files = [os.path.relpath(os.path.join(root, file), main_path) for root, i, files in os.walk(
        main_path) for file in files if file.endswith('.html')]
    for rel_path in files:
        path, file = os.path.split(rel_path)
        test_path = os.path.join(main_path, 'template', path)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.copyfile(os.path.join(main_path,rel_path), os.path.join(new_path, file))
