import os
# PATH = lambda p: os.path.join(os.path.split(os.path.dirname(__file__))[0], p)
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
print(PATH('./apps/HelloFreeMusic.apk'))
