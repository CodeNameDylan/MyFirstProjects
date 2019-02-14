'''
Created on Feb 13, 2019

@author: Dylan
This program creates mad lib poems
'''

import random
article2 = ['the','a','another']
subject = ['dog','cat','riley','mutants']
verb = ['laughed','sang','danced', 'farted']
adverb = ['loudly','faster','excitedly','rapidly']
i=0
while i < 5:
    random_article = random.choice(article2)
    random_subject = random.choice(subject)
    random_verb = random.choice(verb)
    random_adverb = random.choice(adverb)
    print(random_article, " ", random_subject," ", random_verb," ", random_adverb)
    i += 1