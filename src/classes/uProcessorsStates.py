import os
import subprocess
import re


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
        with open(self.rubric) as rubric:
            template = rubric.read()

            for item in os.listdir(self.inDir):
                itemPath = os.path.join(self.inDir, item)
    
                if os.path.isdir(itemPath):
                    fileName = item + '_retroalimentacion.md'
                    filePath = os.path.join(self.outDir, fileName)
    
                    with open(filePath, 'w') as file:
                        splitName = re.findall(r'[A-Z][a-z]*', item[:-2]) # Separate name
                        name = ' '.join(splitName)
                        file.write(f'# Estudiante: {name}\n')
                        file.write(template)
                        print(f'{fileName} was created!')

        self.endProcess = True
        print(
            'All the rubrics are created!\n'
            'Have a nice time grading assignments :)'
            )
        
    def State3(self):

        '''
        This state creates the files 
        '''
        for filename in os.listdir(self.inDir):
            if filename.endswith(".md"):
                pathMD = os.path.join(self.inDir, filename)
                filenamePDF = filename.rsplit(".", 1)[0] + ".pdf"
                pathPDF = os.path.join(self.outDir, filenamePDF)

                subprocess.run(
                    [
                        "pandoc", pathMD,
                        "-o", pathPDF,
                        "--pdf-engine=xelatex",
                        "--columns=1000",
                        "--listings",
                        "-V", "geometry:top=2cm,left=2cm,right=2cm,bottom=2cm",
                        "-V", "fontsize=12pt"
                    ],
                    check=True
                    )
                
                print(
                    f'{filenamePDF} has been created!'
                    )

        print(
            'All pdfs have been created!\n'
            'Have a nice time uploading the files :)'
            )

        self.endProcess = True #added for TESTING
        
