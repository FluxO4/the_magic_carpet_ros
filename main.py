import os
from sys import argv
#ros setup
current_path = os.getcwd()
repos_file = os.path.join(current_path, "setup.repos")
def import_vcs():
    os.system("mkdir -p ./src")
    os.system("vcs import ./src --input " + repos_file)

def build():
    os.system("colcon build")

if __name__ == '__main__':
    if argv[1] == "import":
        import_vcs()
    elif argv[1] == "build":
        build()
    else:
        import_vcs()
        build()
    