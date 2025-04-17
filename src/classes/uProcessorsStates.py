class uProcessorsStates:

    def __init__(self):
        self.rubric = None
        self.inDir = None
        self.outDir = None
        self.presentState = None


    def State1(self):
       
        print('this is the first state, soon to assign the second state')
        self.presentState = self.State2
        
    def State2(self):

        print('this is the second state')
        
