import subprocess
import os

DEFAULT = ".\Video"
if not os.path.exists(DEFAULT):
    os.makedirs(DEFAULT)
os.chdir(DEFAULT)
subprocess.run('youtube-dl --write-auto-sub https://www.youtube.com/watch?v=TmjjHbUb4jc')