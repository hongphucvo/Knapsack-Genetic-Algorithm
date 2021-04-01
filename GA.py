import random
import sys
import operator

#import https://github.com/Pantzan/KnapsackGA/blob/master/knapsack.py
class Knapsack(object):
    def __init__(obj):
        obj.weight=[]#list of weight
        obj.func=[]#list of value
        obj.state=[]#list of state
        obj.F0=[]#generate parent0
        obj.best=[]
        obj.eval=[]#dung parent cung voi fitness
        obj.bestFunc=[]

        
        obj.bagSize=0
        obj.things=0
        obj.population=0
    def defaultState(obj):
        for i in range (0,obj.population):
            parent=[]
            for t in range (0, 5):
                k=random.randint(0,1)
                parent.append(k)
            obj.F0.append(parent)

    def setDetail(obj, w, f,opt, bagSize, population):
        obj.weight=w
        obj.func=f
        obj.state=opt
        obj.bagSize=bagSize
        obj.population=population
        obj.defaultState()

    def fitness(obj, thingsList):
        w=0
        f=0
        for i in enumerate(thingsList):
            if i==0:
                continue
            else:
                w+=obj.weight[i]
                p+=obj.func[i]

        if w>obj.bagSize:
            return -1
        else:
            return f

    def evaluation(obj):
        for i in (obj.F0):
            parent=i
            ft=obj.fitness(parent)
            obj.eval.append((ft,parent))

        best_pop=obj.population//2
        obj.eval.sort()#(key=operator.itemgetter(0), reverse=True)
        obj.bestFunc=obj.eval[:best_pop]
        obj.bestFunc=[x[1] for x in obj.bestFunc]

    def mutation(obj, state):
        for i in range(0, state):
            k=random.uniform(0,1)
            if k>0.5:
                if state[i]==1:
                    state[i]=0
                else:
                    state[i]=0

        return state

    def crossover(obj, papa, mama):
        split=random.randint(1, len(papa)-1)
        elderly=papa[split:]
        youngster=mama[split:]
        elderly.extend(mama[:split])
        youngster.extend(papa[:split])
        return elderly, youngster

    def GA(obj):
        obj.evaluation()
        newparents=[]
        pop=len(obj.bestFunc)-1


        #generating F0
        sample = random.sample(range(pop), pop)
        for i in range(0, pop):
            if i < pop-1:
                r1 = obj.bestFunc[i]
                r2 = obj.bestFunc[i+1]
                nchild1, nchild2 = obj.crossover(r1, r2)
                newparents.append(nchild1)
                newparents.append(nchild2)
            else:
                r1 = obj.bestFunc[i]
                r2 = obj.bestFunc[0]
                nchild1, nchild2 = obj.crossover(r1, r2)
                newparents.append(nchild1)
                newparents.append(nchild2)
        #mutate children
        for i in range(len(newparents)):
            newparents[i] = obj.mutation(newparents[i])
        if obj.state not in newparents:
            print("RUN")
            self.parents = newparents
            self.bests = []
            self.best_p = []
            self.GA()	




weights = [12,  7, 11, 8, 9]
profits = [24, 13, 23, 15, 16]
opt     = [0, 1, 1, 1, 0]
C = 26
population = 10

k = Knapsack()
k.setDetail(weights, profits, opt, C, population)
k.GA()
