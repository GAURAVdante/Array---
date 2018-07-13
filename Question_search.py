#!/usr/bin/env python
from __future__ import print_function


import sys 
import os
import csv
sys.path.append('.')
sys.path.append('..')

try:
    get_input = raw_input
except NameError:
    get_input = input

user_api_key = get_input("Please enter an API key if you have one (Return for none):")
if not user_api_key: user_api_key = None

import stackexchange
so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        term = get_input('Please provide a search term:')
    else:
        term = ' '.join(sys.argv[1:])
    print('Searching for %s...' % term,)
    sys.stdout.flush()

    qs = so.search(intitle=term)
    file = open('d.csv','w',newline='',encoding='utf-8')
    with file:
      print('\r--- questions with "%s" in title ---' % (term))
      for q in qs:
            s = [q.id,q.title,q.score,q.tags,q.answer_count,q.is_answered,q.view_count,q.url,q.link,q.last_activity_date,q.creation_date,q.json]
            writer = csv.writer(file)
            writer.writerow(s)
