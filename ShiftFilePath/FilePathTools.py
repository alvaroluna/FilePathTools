import os
import inspect

class ShiftFilePath:
    """
    Purpose:
        This does something

    Args:
        filePath: str
            *while optional if None, return will be caller method's current directory*
        branchesBack (opt): int--positive int
            *can be 0--no change--or by default it will be sent to 1
        appendPath (opt): str

    Returns:
        str when obj called with method.ToString

    Instructions:
        1) import FilePathTools | from FilePathTools import ShiftFilePath
        2) call ShiftFilePath w/ arguments and .ToString: 
            ShiftFilePath(filePath, branchesBack, subFolderPath).ToString

    Example:
        originalPath = r"C:\\Users\aluna\Documents\Projects\ProjectFolder"
        *if originalPath == None: path = os.path.dirname(__file__)

        newPath = ShiftFilePath(path=originalPath, branchesBack=2, appendPath="Lib").ToString

        print(newpath) --> "C:\\Users\aluna\Documents\Lib"
    """

    def __init__(self, path=None, branchesBack=1, appendPath=None):
        # input parameters
        if path and type(path) is str:
            self.path = path
        elif path and type(path) is not str:
            raise Exception("File path as (str) is needed")
        elif path is None:
            # get file path of caller method
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            self.path = module.__file__

        self.branchesBack = branchesBack
        self.appendPath = appendPath

        # run the shift path method automatically upon instantiation
        self.ToString = self.Run_ShiftFilePath()

    def __repr__(self):
        return("<class 'ShiftFilePath Object'>\nreturn string: class().ToString")

    def Run_ShiftFilePath(self):
        # os environment variable
        osEnv = None

        # reversing string makes it easier to discard
        # the part of the file path being eliminated
        pathReverse = self.path[::-1]
        if "\\" in self.path:
            osEnv = "windows"
            newPathBackwards = pathReverse.split("\\", self.branchesBack)[-1]
        elif "/" in self.path:
            osEnv = "anything else"
            newPathBackwards = pathReverse.split("/", self.branchesBack)[-1]

        # new steped back file path 
        newPath = newPathBackwards[::-1]

        # extend file path with appending string - windows or anything other os
        if type(self.appendPath) is str and osEnv == "windows":
            return(r"{0}\{1}".format(newPath, self.appendPath))
        elif type(self.appendPath) is str and osEnv == "anything else":
            return(r"{0}/{1}".format(newPath, self.appendPath))
        else: return(newPath)

def Test():
    samplePath = r"C:\Users\aluna\Documents"
    newPath = ShiftFilePath(path=samplePath, branchesBack=2  , appendPath="0Lib")
    newNewPath = ShiftFilePath(path=None, branchesBack=2)

    print("Result with path:\n    {0}".format(newPath.ToString))
    print("Result without path:\n    {0}".format(newNewPath.ToString))

if __name__ == "__main__":
    Test()