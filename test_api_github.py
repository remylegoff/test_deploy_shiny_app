from github import Github
import os
# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
#os.chdir("test_chimstat")
# Then play with your Github objects:
repo = g.get_user().get_repo("ChimstatxMWine")
contents = repo.get_contents("")
import shutil

shutil.rmtree('Chimstat')
os.mkdir("Chimstat")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        print(file_content.path)
        if file_content.path not in os.listdir():
            print(file_content.path)
            os.mkdir(file_content.path)
        contents.extend(repo.get_contents(file_content.path))
    else:
        print(file_content.path)
        with open(file_content.path, "wb") as f:
            f.write(file_content.decoded_content)
# To close connections after use
g.close()
os.chdir("Chimstat")
os.mkdir("methodes")
os.mkdir("classifier")
os.mkdir("fusion_donnees")
os.mkdir("graphiques")
os.mkdir("output")
os.mkdir("prediction")
import sys 
sys.path.append(os.getcwd())
from ui import app
app
