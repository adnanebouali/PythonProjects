import datetime
import subprocess
from git import Repo

# Step 1: Get the current date
now = datetime.datetime.now()

# Step 2: Write the date to the text file
with open('D:\myfiles\DailyPush\Thefile.txt' , 'a') as file:
    file.write(f"{now.strftime('%A')} // {now.strftime('%Y-%m-%d')} // {now.strftime('%H:%M:%S')} // {now.strftime('%j')} day of the year.\n")


# Step 3: Use Git to commit and push the changes

PATH_OF_GIT_REPO = r'D:\myfiles\DailyPush\.git' 
COMMIT_MESSAGE = f"{now.strftime('%A')} // {now.strftime('%Y-%m-%d')}"

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()



