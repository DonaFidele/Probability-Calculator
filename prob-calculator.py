#coding:utf-8
import random
class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for bales in kwargs:
            while kwargs[bales]!=0:
                self.contents.append(bales)
                kwargs[bales]-=1

    def draw(self,num):
        if num > len(self.contents):
            return self.contents
        resultat=random.sample(self.contents,num)
        for elem in resultat:
            self.contents.remove(elem)
        return resultat
 
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    M=0;m=0;N=num_experiments
    while num_experiments!=0:
        tire=hat.draw(num_balls_drawn)
        dict={bal:tire.count(bal) for bal in tire}
        for bals in expected_balls:
            if  bals in dict and  dict[bals] >=expected_balls[bals]:
                m+=1
            if m==2:
                M+=1
                m=0
        num_experiments-=1
    #print(M,N)
    return M/N



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)