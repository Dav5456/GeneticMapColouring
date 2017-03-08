#! /usr/bin/env python

from country import *
import numpy as np

def countryColour(name, colours):
    clist = [colours[c.geti()] for c in countries if c.getName() == name]
    if len(clist) > 0:
        return clist[0]
    else:
        print("problem " + name)
        return 0

def conflicts(colours):
    conflicts = 0
    for i in range(len(countries)):
        for border in countries[i].getBorders():
            if colours[i] == countryColour(border, colours):
                conflicts += 1
    return conflicts/2

def addCountry(country):
    countries.append(country)
    country.seti(len(countries) - 1)

def setup():
    global countries
    countries = []
    addCountry(Country("Albania",["Greece","Kosovo","Macedonia","Montenegro"]))
    addCountry(Country("Andorra",["France","Spain"]))
    addCountry(Country("Austria",["Czechia","Germany","Hungary","Italy","Liechtenstein","Slovakia","Slovenia","Switzerland"]))
    addCountry(Country("Belarus",["Latvia","Lithuania","Poland","Russia","Ukraine"]))
    addCountry(Country("Belgium",["France","Germany","Luxembourg","Netherlands"]))
    addCountry(Country("Bosnia and Herzegovina",["Croatia","Montenegro","Serbia"]))
    addCountry(Country("Bulgaria",["Greece","Macedonia","Romania","Serbia","Turkey"]))
    addCountry(Country("Croatia",["Bosnia and Herzegovina","Hungary","Montenegro","Serbia","Slovenia"]))
    addCountry(Country("Cyprus",["United Kingdom"]))
    addCountry(Country("Czechia",["Austria","Germany","Poland","Slovakia"]))
    addCountry(Country("Denmark",["Germany"]))
    addCountry(Country("Estonia",["Latvia","Russia"]))
    addCountry(Country("Finland",["Norway","Sweden","Russia"]))
    addCountry(Country("France",["Andorra","Belgium","Germany","Italy","Luxembourg","Monaco","Spain","Switzerland"]))
    addCountry(Country("Germany",["Austria","Belgium","Czechia","Denmark","France","Luxembourg","Netherlands","Poland","Switzerland"]))
    addCountry(Country("Greece",["Albania","Bulgaria","Macedonia","Turkey"]))
    addCountry(Country("Hungary",["Austria","Croatia","Romania","Serbia","Slovakia","Slovenia","Ukraine"]))
    addCountry(Country("Iceland",[]))
    addCountry(Country("Ireland",["United Kingdom"]))
    addCountry(Country("Italy",["Austria","France","San Marino","Slovenia","Switzerland","Vatican City"]))
    addCountry(Country("Kosovo",["Albania","Macedonia","Montenegro","Serbia"]))
    addCountry(Country("Latvia",["Belarus","Estonia","Lithuania","Russia"]))
    addCountry(Country("Liechtenstein",["Austria","Switzerland"]))
    addCountry(Country("Lithuania",["Belarus","Latvia","Poland","Russia"]))
    addCountry(Country("Luxembourg",["Belgium","France","Germany"]))
    addCountry(Country("Macedonia",["Albania","Bulgaria","Greece","Kosovo","Serbia"]))
    addCountry(Country("Malta",[]))
    addCountry(Country("Moldova",["Romania","Ukraine"]))
    addCountry(Country("Monaco",["France"]))
    addCountry(Country("Montenegro",["Albania","Bosnia and Herzegovina","Croatia","Kosovo","Serbia"]))
    addCountry(Country("Netherlands",["Belgium","Germany"]))
    addCountry(Country("Norway",["Finland","Sweden","Russia"]))
    addCountry(Country("Poland",["Belarus","Czechia","Germany","Lithuania","Russia","Slovakia","Ukraine"]))
    addCountry(Country("Portugal",["Spain"]))
    addCountry(Country("Romania",["Bulgaria","Hungary","Moldova","Serbia","Ukraine"]))
    addCountry(Country("Russia",["Belarus","Estonia","Finland","Latvia","Lithuania","Norway","Poland","Ukraine"]))
    addCountry(Country("San Marino",["Italy"]))
    addCountry(Country("Serbia",["Bosnia and Herzegovina","Bulgaria","Croatia","Hungary","Kosovo","Macedonia","Montenegro","Romania"]))
    addCountry(Country("Slovakia",["Austria","Czechia","Hungary","Poland","Ukraine"]))
    addCountry(Country("Slovenia",["Austria","Croatia","Italy","Hungary"]))
    addCountry(Country("Spain",["Andorra","France","Portugal","United Kingdom"]))
    addCountry(Country("Sweden",["Finland","Norway"]))
    addCountry(Country("Switzerland",["Austria","France","Germany","Liechtenstein","Italy"]))
    addCountry(Country("Turkey",["Bulgaria","Greece"]))
    addCountry(Country("Ukraine",["Belarus","Hungary","Moldova","Poland","Romania","Russia","Slovakia"]))
    addCountry(Country("United Kingdom",["Cyprus","Ireland","Spain"]))
    addCountry(Country("Vatican City",["Italy"]))
    
def getBest(colourses):
    best = []
    scores = []
    for colours in colourses:
        scores.append(conflicts(colours))
    for x in range(5):
        pos = np.argmin(scores)
        best.append(colourses[pos])
        del scores[pos]
        del colourses[pos]
    return best

def eugenics(p0, p1):
    child = []
    for i in range(len(p0)):
        gene = np.random.randint(low=0,high=2)
        if gene == 0:
            child.append(p0[i])
        else:
            child.append(p1[i])
    return child

def getChildren(colourses):
    children = []
    parents = getBest(colourses)
#    print conflicts(parents[0])
    for x in range(5):
        for y in range(5-x):
            for z in range(5):
                children.append(eugenics(parents[x],parents[y]))
    return children

def gmc(num, iterations):
    colourses = []
    for x in range(50):
        colours = list(np.zeros(len(countries),dtype=np.int))
        for i in range(len(countries)):
            colours[i] = np.random.randint(low=0,high=num)
        colourses.append(colours)
    for i in range(iterations):
        colourses = getChildren(colourses)
    best = getBest(colourses)[0]
#    print [(countries[i].getName(), best[i]) for i in range(len(best))]
    return conflicts(best)

def main():
    setup()
    score = 1
    counter = 0
    c = 4
    while score > 0:
        score = gmc(c,10)
        counter += 1
        if counter == 50:
            c += 1
            counter = 0
    print "success " + str(c) + " " + str(counter)

main()