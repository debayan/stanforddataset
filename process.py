#!/usr/bin/python


import sys,os,json
from sets import Set

set = Set()

f = open('kvret_train_public.json')

s = f.read()

dialogues = json.loads(s)

for dialogue in dialogues:
    placeholders = {}
    try:
        for item in dialogue['scenario']['kb']['items']:
            for k,v in item.iteritems():
                placeholders[v] = k
    except Exception,e:
        pass
    try:
        for turn in dialogue['dialogue']:
            #print turn
            if turn['turn'] == 'assistant':
                for k,v in turn['data']['slots'].iteritems():
                    placeholders[v] = k
                l = turn['data']['utterance']
                for k,v in placeholders.iteritems():
                    if k in l:
                        l = l.replace(k,'<'+v+'>')
                #print l
                set.add(l)
    except Exception,e:
        pass
            
for item in set:
    print item
