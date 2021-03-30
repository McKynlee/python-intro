# python-intro

## Installing Python 
### (this section compliments of Prime Digital Academy)
MacOS already has a version of python installed. However it is likely a version of python 2 and you will want to be working with python 3.

Homebrew Python Install
Install python version 3:

brew install python
If you get the following Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks, it can be fixed by doing the following:

sudo mkdir /usr/local/Frameworks
sudo chown $USER /usr/local/Frameworks
If sudo isn't allowed, you can also try:

install -d -o $(whoami) -g admin /usr/local/Frameworks

Then,

brew reinstall python

Running
Homebrew sets up python 3 as a separate executable, which keeps it from conflicting with the MacOS version. That's awesome, but means instead of using python and pip you need to run python3 and pip3.

Pip is the package manager for Phython, like npm for Node.

Check that they both work:

python3 --version
pip3 --version




## Using VS Code with Python 
1. Open a new repository in VS Code.

1. Install the Python Extension in VS Code: ms-python.python

1. Set up your environment: Select your Python interpreter from the VS Code: 
Open the Command Palette (⇧⌘P), use command 'Python: Select Interpreter', and choose the Python version from the available list that best matches the Python version you downloaded.

1. VS Code may prompt you with additional installations for your Python environment, depending on your current setup.  Follow these suggestions and install the necessary tools.

1. Save new Python files with the .py suffix, so that VS Code knows it is a Python file and will use the Python Interpreter with it.

1. To run your .py code, 4 options:
    ii. Click the right-facing "play" triangle at the top right of your .py file in VS Code (this is located directly to the left of the Split Screen double box button and the "...").
    ii. Right click anywhere in the editor window, and select "Run Python File in Terminal" (note, there is also an option to run the code in and Interactive Window- this is NOT what we are looking for!).
    ii. Select the lines you want to run and press Shift+Enter.
    ii. Open your Command Palette (⇧⌘P) and access the Python: Start REPL command.  This will open an REPL terminal for the current Python Interpreter you selected.  You can enter and run lines of code directly in the REPL terminal.



