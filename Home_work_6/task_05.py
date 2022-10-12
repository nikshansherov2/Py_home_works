# Выводит на экран N шуток, сформированных из трех случайных слов,
# взятых из трёх списков.

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "человек", "медведь"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "угловатый", "наглый"]


def create_jokes(nouns, adverbs, adjectives, number):
    jokes = [choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives) for i in range(number)]
    return jokes


print('Ваши шутки:\n', create_jokes(nouns, adverbs, adjectives,
                                   int(input('Введите количество шуток: '))))
