import os
from os import path
if path.exists("env.py"):
    import env

MongoCon = os.environ.get('MongoCon')

print(MongoCon)
