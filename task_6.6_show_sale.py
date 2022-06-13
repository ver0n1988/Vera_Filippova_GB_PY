bakery = "./bakery.csv"

def show_file(start=-1, end=-1):

    with open(bakery, 'r', encoding='utf-8') as file_1:

        if start > 0:
            for i in range(start - 1):
                file_1.readline()


        if end > 0:
            for i in range(abs(end - start) + 1):
                yield file_1.readline().replace('\n', '')
        else:
            for line in file_1:
                yield line.replace('\n', '')

        for line in file_1:
            yield line.replace('\n', '')


import sys

start_pos = -1
end_pos = -1

if len(sys.argv) >= 2 and sys.argv[1].isdigit():
    start_pos = int(sys.argv[1])

if len(sys.argv) == 3 and sys.argv[2].isdigit():
    end_pos = int(sys.argv[2])

for l in show_file(start_pos, end_pos):
    print(f'{float(l):.2f}')