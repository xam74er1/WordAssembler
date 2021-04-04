class Composition:


    def __init__(self,positive = [],negative=[],result="",pts=0):
        self.positive = positive
        self.negative = negative
        self.pts = pts
        self.result = result


    def parse(self,ligne="",delimiter=";"):
        #On les resete car si non il gare les ancine valleur (aucune idee de pourquoi ce bug )
        self.positive = []
        self.negative = []
        self.result = ""
        self.pts = 0;


        ligne = ligne.replace("\n","");
        tab = ligne.split(delimiter);
        cnt = 0
        #On list les 4 pemire ellment qui son les mot positive
        for i in range(4):
            w = tab[cnt]
            #Si le mot n'est pas null
            if(len(w)>0):
                self.positive.append(w)
            cnt = cnt+1;

        #On list les 2 mot suivant qui son des negatie
        for i in range(2):
            w = tab[cnt]
            #Si le mot n'est pas null
            if(len(w)>0):
                self.negative.append(w)
            cnt = cnt+1;

        #On list le resulta
        w = tab[cnt]
        self.result=w
        cnt = cnt + 1;

        #ON lit le nbr de pts
        w = tab[cnt]
        self.pts = int(w)


