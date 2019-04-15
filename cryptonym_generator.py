import random
import re
from sys import stdout
from typing import List, Tuple

from nltk.corpus import wordnet as wn


#nouns = open('nouns.txt').read().splitlines()
#adjectives = open('adjectives.txt').read().splitlines()



def iter_flatten(iterable: List) -> List:
  it = iter(iterable)
  for e in it:
    if isinstance(e, (list, tuple)):
      for f in iter_flatten(e):
        yield f
    else:
      yield e


def no_bad_chars(string: str) -> bool:
    #return '-' not in string and '_' not in string
    return re.search(r'[\W_]', string) == None

def initialize() -> Tuple:
    wn_nouns = [x.lemma_names() for x in list(wn.all_synsets('n'))]
    wn_adjectives = [x.lemma_names() for x in list(wn.all_synsets('a'))]
    filtered_nouns = list(filter(no_bad_chars, iter_flatten(wn_nouns)))
    filtered_adjectives = list(filter(no_bad_chars, iter_flatten(wn_adjectives)))
    return (filtered_adjectives, filtered_nouns)

def random_pair(adjectives: List, nouns: List) -> tuple:
    return (random.choice(adjectives), random.choice(nouns))



if __name__ == '__main__':
    print("Populating word bank...")
    adjectives, nouns = initialize()
    selection = None
    while selection != 'q':
        a, b = random_pair(adjectives, nouns)
        print("{} {}".format(a.lower(), b.lower()))
        selection = input("Enter to regenerate, or (q) to quit.")