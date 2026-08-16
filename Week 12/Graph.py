class Graph:
    #slots will restrict the class attributes
    __slots__ = ['__xcoor', '__ycoor']

    # creating an initialization function called constructor here
    def __init__(self, xcoor, ycoor):
        self.__xcoor = xcoor
        self.__ycoor = ycoor

    # accessor function (means using which we can access the value of private attributes)
    def getXCoor(self):
        return self.__xcoor
    
    def getYCoor(self):
        return self.__ycoor
    
    #mutator function (means using which we can set the value of private attributes)
    def setXCoor(self, newXCoorValue):
        self.__xcoor = newXCoorValue

    def setYCoor(self, newYCoorValue):
        self.__ycoor = newYCoorValue

    #representing the output as string using special method __str__
    def __str__(self):
        return "#####The value of xcoor is: " + str(self.getXCoor()) + " and the value of ycoor is " + str(self.__getattribute__etYCoor())
    
    def __repr__(self):
        return "The value of xcoor is: " + str(self.getXCoor()) + " and the value of ycoor is " + str(self.__getattribute__etYCoor())

    #special method __eq__ to check the equality of 2 object values
    def __eq__(self, other):
        if type(self) == type(other):
            return  self.__xcoor==other.__xcoor
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other) 
    
    def __lt__(self,other):
        if type(self) == type(other):
            return  self.__xcoor==other.__xcoor
        else:
            return False


def main():
    #creating an instance/object of Graph class
    graph1 = Graph(10,8)
    print(graph1.getXCoor())
    print(graph1.getYCoor())
    #graph1__xcoor = 15
    graph1.setXCoor(15)
    print("After setting new value for xcoor: ", graph1.getXCoor())
    graph1.setXCoor(88)
    print("After setting new value for ycoor: ", graph1.getYCoor())

    print(graph1)
    #creating another instance below
    graph2 = Graph(15,4)

    # we want to check whether instance 1 xcoor value is equal to instance 2 xcoor value

    print(graph1==graph2) # this statement will find if there is an __eq__ funciton in the class, if yes pls execute that, if no pls compare memory addresses
    print(graph1!=graph2)

    print(graph1<=graph2)
main()


#create a dictionary with graph objects as keys 
    performance={
        graph1:"normal coordinator",
        graph2:"ordanary coordinators"
    }

    #attempt to add a duplicate graph 
    graph_duplicate=Graph(16,4)
    performance[graph_duplicate]="Needs cooridnates"