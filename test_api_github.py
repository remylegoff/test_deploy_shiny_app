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
if 'methodes' not in os.listdir(os.getcwd()):
    os.mkdir('methodes')
if 'classifier' not in os.listdir(os.getcwd()):
    os.mkdir('classifier')
if 'output' not in os.listdir(os.getcwd()):
    os.mkdir('output')  
if 'prediction' not in os.listdir(os.getcwd()):
    os.mkdir('prediction')  
if 'graphiques' not in os.listdir(os.getcwd()):
    os.mkdir('graphiques')  
    os.mkdir('graphiques/3D')
    os.mkdir('graphiques/2D')
    os.mkdir('graphiques/Screeplot')
    os.mkdir('graphiques/Contributions')
    os.mkdir('graphiques/Predictions')
    os.mkdir('graphiques/Clustering')
    os.mkdir('graphiques/Confiance')

import sys 
sys.path.append(os.getcwd())
from ui import app
app
