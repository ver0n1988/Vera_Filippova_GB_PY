from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(n, flag=False):
    for i in range(n):
        random_noun=choice(nouns)
        random_adv=choice(adverbs)
        random_adj=choice(adjectives)
        joke=f'{random_noun} {random_adv} {random_adj}'
        jokes_list=[]
        print(joke)
        if flag==True:
            for noun in nouns:
                for word in jokes_list:
                    if noun==word:
                        nouns.remove(noun)
            for adverb in adverbs:
                for word in jokes_list:
                    if adverb==word:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for word in jokes_list:
                    if adjective==word:
                        adjectives.remove(adjective)


get_jokes(n=3, flag=True)
