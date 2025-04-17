import os


class uProcessorsStates:

    def __init__(self):
        self.rubric = None
        self.inDir = None
        self.outDir = None
        self.presentState = None
        self.typeProcess = None
        self.endProcess = False


    def State1(self):

        '''
        This state checks to see if filepaths exist
        '''
        paths = []
        match self.typeProcess:
            case 'md':
                self.presentState = self.State2
                paths.append(self.rubric)
                paths.append(self.inDir) 
                paths.append(self.outDir)
            case 'pdf':
                self.presentState = self.State3
                paths.append(self.inDir) 
                paths.append(self.outDir)

        for i in paths:
            if os.path.exists(i):
                print(
                    f'Valid filepath for {i}    :)'
                    )
            else:
                print(
                    f'Invalid filepath. Check {i} and run it again    :('
                    )
                self.endProcess = True

        
    def State2(self):

        '''
        This state creates the files for review
        '''

        print('this is the second state')
        self.endProcess = True #added for TESTING
        
    def State3(self):

        '''
        This state creates the files 
        '''

        print('this is the Third state')
        self.endProcess = True #added for TESTING
        
