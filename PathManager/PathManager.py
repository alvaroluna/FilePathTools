import os
import inspect

class ShiftFilePath:
    """
    Purpose:
        This does something

    Args:
        filePath: str
            *while optional if None, return will be caller method's current filePath*
        levelsUp (opt): int--positive int
            *can be 0--no change--or by default it will be sent to 1
        appendPath (opt): str

    Returns:
        str when obj called with method.ToString

    Instructions:
        1) import PathManager | from PathManager import ShiftFilePath
        2) call ShiftFilePath w/ arguments and .ToString: 
            ShiftFilePath(filePath, levelsUp, subFolderPath).ToString

    Example:
        originalPath = r"C:\\Users\aluna\Documents\Projects\ProjectFolder"
        *if originalPath == None: filePath = os.filePath.dirname(__file__)

        newPath = ShiftFilePath(filePath=originalPath, levelsUp=2, appendPath="Lib").ToString

        print(newpath) --> "C:\\Users\aluna\Documents\Lib"
    """

    def __init__(self, levelsUp=1, filePath=None, appendPath=None):
        # input parameters
        self.levelsUp = levelsUp
        self.appendPath = appendPath        
        
        # input parameters with conditionals
        if filePath is None:
            # get file filePath of caller method
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            self.filePath = module.__file__        
        elif filePath and type(filePath) is str:
            self.filePath = filePath
        elif filePath and type(filePath) is not str:
            raise Exception("File filePath as (str) is needed")
        
        # run the shift filePath method automatically upon instantiation
        self.ToString = self.Run_ShiftFilePath()

    def __repr__(self):
        return("<class 'ShiftFilePath Object'>\nreturn string: class().ToString")

    def Run_ShiftFilePath(self):
        # os environment variable
        osEnv = None

        # reversing string makes it easier to discard
        # the part of the file filePath being eliminated
        pathReverse = self.filePath[::-1]
        if "\\" in self.filePath:
            osEnv = "windows"
            newPathBackwards = pathReverse.split("\\", self.levelsUp)[-1]
        elif "/" in self.filePath:
            osEnv = "anything else"
            newPathBackwards = pathReverse.split("/", self.levelsUp)[-1]
        # new steped back file filePath 
        newPath = newPathBackwards[::-1]

        # extend file filePath with appending string
        # (windows or anything other os)
        if type(self.appendPath) is str and osEnv == "windows":
            return(r"{0}\{1}".format(newPath, self.appendPath))
        elif type(self.appendPath) is str and osEnv == "anything else":
            return(r"{0}/{1}".format(newPath, self.appendPath))
        else: return(newPath)

def Test():
    # running tool and leaving filePath=None will
    # automatically use the caller method's directory --> "C:\Users\Username\Documents\Folder\SubFolder\callerFileName.py"
    #                                                     |_________________file directory______________|
    adjustedPath = ShiftFilePath(levelsUp=2).ToString
    print(adjustedPath)
    
    #                                   <--|---2--|----1----|
    #          "C:\Users\Username\Documents\Folder\SubFolder"
    # returns: "C:\Users\Username\Documents
    
    samplePath = None
    
    newPath = ShiftFilePath(levelsUp=2, filePath=samplePath, appendPath="0Lib").ToString
    newNewPath = ShiftFilePath(levelsUp=2, filePath=None).ToString

    print("Result with custom filePath:\n    {0}".format(newPath))
    print("Result without filePath:\n    {0}".format(newNewPath))

if __name__ == "__main__":
    Test()