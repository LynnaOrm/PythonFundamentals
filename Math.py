class Mathdojo(object):

    def __init__(self):

        self.result=0

    

    def add(self, *inPutNo):

        for i in inPutNo:

            if isinstance(i,int): 

                self.result=self.result+i

                print "adding numbers " ,self.result

            else:

                for numBer in i:

                    self.result=self.result + numBer

                    print "adding number", self.result

        return self



    def subtract(self, *inPutNo):

        for i in inPutNo:

            if isinstance(i,int):

                self.result=self.result-i

                print "subtracting number", self.result

            else:

                for numBer in i:

                    self.result=self.result - numBer

                    print "subtracting number",self.result



        return self

#PART I result

md=Mathdojo()               

md.add(2).add(2,5).subtract(3,2).result







#PART II result

md=Mathdojo()         

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result         