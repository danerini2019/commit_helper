from datetime import datetime
from threading import Timer
import subprocess

x=datetime.today()
y=x.replace(day=x.day+1, hour=12, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def comitter():

    subprocess.call(['sh', './committer.sh'])
    #!/bin/sh -e
    commit_message="$1"
    git add . -A
    git commit -m "$commit_message"
    git push

t = Timer(secs, hello_world)
t.start()