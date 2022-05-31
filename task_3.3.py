def thesaurus(*args):
    res = {}
    for name in args:
        if res.get(name[0]):
            res[name[0]].append(name)
        else:
            res[name[0]]=[name]
    return res


#print (thesaurus('Иван', 'Мария', 'Илья', 'Игорь','Марина','Милана'))