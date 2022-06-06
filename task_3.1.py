Dictionary={
    'zero':'ноль',
    'one':'один',
    'two':'два',
    'three':'три',
    'four':'четыре',
    'five':'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'девять',
}


def translate_num(numeral):
    return Dictionary.get(numeral)
    """конвертировать "one" в "один", "two" в "два" и т.д."""
#print(translate_num('nine'))


