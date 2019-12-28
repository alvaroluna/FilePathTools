# PathManager
PathManager is a module that allows you to input a file path and move up n-levels towards the root directory. In addition, you have the option of appending a string to the output if you need to access subfolders originating a level above from the current file's location in a directory. A safer distribution when the distance files are from each other are consistent, but the user's installation location may be different and the code can't rely on exact locations.

For example:

    2 levels up:
    
                         <--|---2--|----1---|
    C:\Users\aluna\Documents\Folder\SubFolder --> C:\Users\aluna\Documents
    
    
    [...] + "Lib\pythonFile.py":
    
                         <--|---2--|----1---|
    C:\Users\aluna\Documents\Folder\SubFolder --> C:\Users\aluna\Documents\Lib\pythonFile.py
                                                                          |____appended____|

This was created because there wasn't a way to describe where dependent python files were in a folder that was shared by several tools. This makes sense if you are form the architecture/design technology world and have worked with PyRevit. At any rate, others may find this tool useful so it has been made available to anyone. Please comment and share, and email me with any recommendations about features that you would like, or bugs that need to be addressed.

## Getting Started

```
originalPath = r"C:\\Users\aluna\Documents\Projects\ProjectFolder"

newPath = ShiftFilePath(path=originalPath, branchesBack=2, appendPath="Lib").ToString
print(newpath) --> "C:\\Users\aluna\Documents\Lib"
```

The preferred method of installation is to use pip install PathManager. Conversely, you may also fork this repo and reference the PathManager.py file directly in your code.

### Prerequisites

There are no 3rd party or external modules that need to be downloaded to get this tool to work. All the modules used in this tool are part of the standard libraries for Python 2, Python 3, and IronPython.

### Installing

```
$ pip install PathManager
```

## Built With

* [Python 3](https://www.python.org/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Alvaro Luna** | [Obj.App](https://objectiveapplications.com/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details