from os import getcwd
from typing import List

from model.Composition import Composition


class CompositionGenerator:
    #listFile = []
    #listComposition:List[Composition] = []
    def __init__(self,listFile):
        self.listFile = listFile
        self.listComposition = []

    def generate(self):
        for f in self.listFile:
            file1 = open('ressource/'+str(f), 'r')
            # On skip la premiere ligne
            line = file1.readline();
            # On ce positione sur la 2nd
            line = file1.readline();
            while line:
                #print(line)

                compo = Composition();
                compo.parse(line)
                #On rajoute la composition
                self.listComposition.append(compo)
                line = file1.readline();

    def getWordFormate(self,positive,negative):
        res : Composition = self.getWord(positive,negative)
        toReturn = {}

        if res != None:
            toReturn["word"] = [res.result,res.pts]
        else :
            toReturn["word"] = ["",0]
        return  toReturn

    #Recupere le mot pour le quelle sa marche
    def getWord(self,positive,negative):
        for compo in self.listComposition:
            if set(compo.positive) == set(positive) and set(compo.negative) == set(negative):
                return compo
        return None;

    #On recupere tout les mot qui n'apparaise pas en reuslta (aka qui son des depare)
    def firstWorld(self):
        list = [];

        #On commence par recupere tout les mot
        mySet = set()
        resSet = set()

        for compo in self.listComposition:
            for w in compo.positive:
                mySet.add(w);
            for w in compo.negative:
                mySet.add(w);
            resSet.add(compo.result)

        #Pour chaque mot on verifie si il n'apparias pas dans les resulta
        for w in mySet:
            #Si il n'apparais pas en result aon l'ajoute
            if(not w in resSet):
                list.append(w)
        return list