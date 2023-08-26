'''
Samantha Ho
Movie Project
CS130R
4/11
'''

#Creation of global variables 
dictionaryMovie = None
dictionaryActors = None 

#opening movies file and make dictionary of actor key and movie key
def openFile():
    global dictionaryMovie
    global dictionaryActors
    textFile = open("movieData.txt")
    dictionaryActors = {}
    for ln in textFile:
        movieList = ln.strip().split(", ") 
        key = movieList[0] 
        dictionaryActors[key]=set(movieList[1:])
    dictionaryMovie = {}
    for actor, movies in dictionaryActors.items():
        for movie in movies:
            if movie in dictionaryMovie.keys():
                dictionaryMovie[movie].add(actor)
            else:
                dictionaryMovie[movie] = [actor]
            dictionaryMovie[movie] = set(dictionaryMovie[movie])

#finding coactors and movies of a given actor 
def searchActors(actor):
    result = set()
    for movie in dictionaryMovie.keys():
        if actor in dictionaryMovie[movie]:
            result = result.union(dictionaryMovie[movie])
    result.remove(actor)
    result = list(result)
    i=0
    bothStarring = set()
    for i in range(0,len(result)):
        bothStarring =(dictionaryActors[actor].intersection(dictionaryActors[result[i]]))
        i+=1
    print(result)
    print("Shared movie titles: ", bothStarring)
    print()

#prompt for user input, determine which dictionary we look at, differentiating operator and performing       
def Main():
    openFile()
    i = 0
    while i ==0:
        command = input("Enter command: ")
        if "&" in command:
            item = command.strip().split("&")
            itemStrip = item[0].strip()
            itemStrip2 = item[1].strip()
            if itemStrip and itemStrip2 in dictionaryMovie.keys():
                commonActors=dictionaryMovie[itemStrip].intersection(dictionaryMovie[itemStrip2])
                if commonActors != set():
                    print(commonActors)
                    print()
                else:
                    print("No common actors")
                    print()
            elif itemStrip and itemStrip2 in dictionaryActors.keys():
                bothStar =dictionaryActors[itemStrip].intersection(dictionaryActors[itemStrip2])
                if bothStar != set():
                    print(bothStar)
                    print()
                else:
                    print("No common movies")
                    print()
            else:
                print("Please enter valid input!!")
                print()
        elif "^" in command:
            item = command.strip().split("^")
            itemStrip = item[0].strip()
            itemStrip2 = item[1].strip()
            if itemStrip and itemStrip2 in dictionaryMovie.keys():
                sepActor=dictionaryMovie[itemStrip].symmetric_difference(dictionaryMovie[itemStrip2])
                if sepActor != set():
                    print(sepActor)
                    print()
                else:
                    print("All same actors.")
                    print()
            elif itemStrip and itemStrip2 in dictionaryActors.keys():
                sepStar=dictionaryActors[itemStrip].symmetric_difference(dictionaryActors[itemStrip2])
                if sepStar != set():
                    print(sepStar)
                    print()
                else:
                    print("No exclusive movies.")
                    print()
            else:
                print("Please enter valid input.")
                print()
        elif "|" in command:
            item = command.strip().split("|")
            itemStrip = item[0].strip()
            itemStrip2 = item[1].strip()
            if itemStrip and itemStrip2 in dictionaryMovie.keys():
                eitherActor=dictionaryMovie[itemStrip].union(dictionaryMovie[itemStrip2])
                print(eitherActor)
                print()
            elif itemStrip and itemStrip2 in dictionaryActors:
                eitherStar=dictionaryActors[itemStrip].union(dictionaryActors[itemStrip2])
                print(eitherStar)
                print()
            else:
                print("Please enter valid input.")
                print()
        else:
            actor = command.strip()
            if actor in dictionaryActors.keys():
                searchActors(actor)
            else:
                print("Please enter valid actor name")
                print()
        
 

Main()



        
