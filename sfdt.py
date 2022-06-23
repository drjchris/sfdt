from datetime import datetime
from hashlib import md5
from typing import Dict
from pandas import DataFrame
from numpy import cumsum
from json import loads

# created a simple list of dates
def listDates(sdate: str, edate: str) -> list:
    start_date = datetime.strptime(sdate.strip(), '%Y-%m-%d')
    end_date = datetime.strptime(edate.strip(), '%Y-%m-%d')
    outlist = [datetime.strptime('%2.2d-%2.2d' % (y, m), '%Y-%m').strftime('%Y-%m-01')
        for y in range(start_date.year, end_date.year + 1)
        for m in range(start_date.month if y == start_date.year else 1, end_date.month + 1 if y == end_date.year else 13)]
    return outlist

# simple value counter returns for dataframe
def countValues(rawlist: list) -> list:
    interdict = {}
    for inval in sorted(list(set(rawlist))):
        interdict[inval] = 0
    for eval in rawlist:
        interdict[eval]+=1
    outlist = []
    for eent in interdict:
        outlist.append({'value': eent, 'count': interdict[eent]})
    #sortlistout = 
    return sorted(outlist, key=lambda item: item.get("count"), reverse=True)
    #return sortlistout

# anonymises a string by implementing md5 thing
def makeAnon(theInput: str) -> str:
    return md5(theInput.encode()).hexdigest()

# calculates full community structure
def commStruct(rawList: list) -> Dict:

    # count the values
    theCount = countValues(rawList)

    # pass on to dataframe
    outdf = DataFrame(theCount)

    # add pc and cpc
    outdf['pc'] = outdf['count']/sum(outdf['count'])
    outdf['cpc'] = cumsum(outdf['pc'])

    # apply layers
    outdf['layer'] = 3
    outdf.loc[outdf['cpc']<0.666666, 'layer'] = 2
    outdf.loc[outdf['cpc']<0.333333, 'layer'] = 1
    outdf.loc[0,'layer'] = 1

    # declare output dictionary
    fullDict = {
        'core': list(outdf['value'][outdf['layer']==1]),
        'mid': list(outdf['value'][outdf['layer']==2]),
        'per': list(outdf['value'][outdf['layer']==3]),
        'data': loads(outdf.to_json(orient="records"))
    }

    return fullDict
