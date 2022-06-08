#task 5.1
def odd_num(max_num):
    for i in range(1, max_num+1,2):
        yield i
        

#task 5.2
def new_odd_num(max_num):
    return(x for x in range(1, max_num+1,2))


if __name__=='__main__':
    a=odd_num(15)
    b=new_odd_num(15)
    print('a type ', type(a))
    print('b type ', type(b))

    for j in a:
        print(j)

