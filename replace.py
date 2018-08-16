#!/usr/bin/python

import sys,os,json
from sets import Set

placeholder = {}

f1 = open('utterances.txt')
f2 = open('kvret_train_public.json')

s = f2.read()
dialogues = json.loads(s)

for dialogue in dialogues:
    try:
        for item in dialogue['scenario']['kb']['items']:
            for k,v in item.iteritems():
                placeholder[v] = k
    except Exception,e:
        pass
        #print e
        #print dialogue

for dialogue in dialogues:
    for turn in dialogue['dialogue']:
        try:
            for k,v in turn['data']['slots'].iteritems():
                placeholder[v] = k
        except Exception,e:
            print e

f2.close()
set = Set()
for line in f1.readlines():
    l = line
    print l
    for k,v in placeholder.iteritems():
        if k in l:
            l = l.replace(k,'<'+v+'>')
            print l
    set.add(l)
    #print l

print len(set)
print len(placeholder)
        
