#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

""" Exemple de ligne:
C0000005|ENG|P|L0000005|PF|S0007492|Y|A7755565||M0019694|D012711|MSH|
PEN|D012711|(131)I-Macroaggregated Albumin|0|N||
"""

""" Pour cette ligne, explication:

    cui = C0000005 -> Unique identifier for concept
    lat = ENG -> Language of term
    ts = P -> Term status
    lui = L0000005 -> Unique identifier for term
    stt = PF -> String type
    sui = S0007492 -> Unique identifier for string
    ispref = Y -> Atom status preferred (Y/N)
    aui = A7755565 -> Unique identifier for atom
    saui = '' -> Source asserted atom identifier
    scui = M0019694 -> Source asserted concept identifier
    sdui = D012711 -> Source asserted descriptor identifier
    sab = MSH -> Abbreviated source name
    tty = PEN -> Abbreviation for term type in source vocabulary
    code = D012711 -> Most useful source asserted identifier
    string = (131)I-Macroaggregated Albumin -> String
    srl = 0 -> Source restriction level
    suppress = N -> Suppressible flag
    cvf = '' - Content View Flag

"""


def checkThesaurus(filePath, size):
    print('Checking the thesaurus file...')
    ok = False
    if os.path.isfile(filePath):
        with open(filePath, encoding='utf-8') as f:
            if sum(1 for line in f) == size:
                f.seek(0)
                l = f.readline().split('|')
                if len(l) == 2 and l[1][0] == 'C':
                    ok = True
    if ok:
        print('Your thesaurus is up to date.')
    else:
        print('Your thesaurus file is incorrect.')
    return(ok)


def createThesaurus(rThesaurus, fThesaurus):
    print('Generating new thesaurus file (this can take a while)...')
    rawThesaurus = open(rThesaurus, 'r', encoding='utf-8')
    formattedThesaurus = open(fThesaurus, 'w', encoding='utf-8')
    forbidden = ['[']
    ft = []
    for line in rawThesaurus:
        temp = line.split('|')
        if(len(temp[14]) > 1 and temp[14][0] not in forbidden):
            if temp[1] == 'FRE' or temp[1] == 'ENG':
                ft.append(temp[14] + '|' + temp[0] + '\n')
    ft = list(set(ft))
    for i in ft:
        formattedThesaurus.write(i)
    print("Your thesaurus is now up to date.")
    rawThesaurus.close()
    formattedThesaurus.close()


def createThesaurusHardcore(rThesaurus, fThesaurus):
    print('Generating new thesaurus file (this can take a while)...')
    rawThesaurus = open(rThesaurus, 'r', encoding='utf-8')
    formattedThesaurus = open(fThesaurus, 'w', encoding='utf-8')
    forbidden = ['[']
    ft = []
    for line in rawThesaurus:
        temp = line.split('|')
        if(len(temp[14]) > 2 and temp[14][0] not in forbidden):
            if temp[1] == 'FRE' or temp[1] == 'ENG':
                ft.append(temp[14] + '|' + temp[0] + '\n')
    ft = list(set(ft))
    for i in ft:
        formattedThesaurus.write(i)
    print("Your thesaurus is now up to date.")
    rawThesaurus.close()
    formattedThesaurus.close()
