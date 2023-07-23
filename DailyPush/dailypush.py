import datetime
import subprocess
from git import Repo


now = datetime.datetime.now()
PATH_OF_GIT_REPO = r'D:\myFiles\DailyPush' 
COMMIT_MESSAGE = f"{now.strftime('%A')} // {now.strftime('%Y-%m-%d')}"
repo = Repo(PATH_OF_GIT_REPO)
origin = repo.remote(name='origin')
origin.pull()

with open('D:\myFiles\DailyPush\Thefile.txt' , 'a') as file:
    file.write(f"{now.strftime('%A')} // {now.strftime('%Y-%m-%d')} // {now.strftime('%H:%M:%S')} // {now.strftime('%j')} day of the year.\n")

def git_push():
    try:
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()



