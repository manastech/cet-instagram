# -*- coding: utf-8 -*-
## Imports
from InstagramAPI import Instagram
import csv
import sys
import os


if(len(sys.argv) < 5):
  print("Los parámetros deben ser: <username> <password> <archivo.csv> <mensaje>")
  sys.exit(2)


## Config data
username = sys.argv[1]
password = sys.argv[2]
debug = True

settings_dir = "./data/"
if not os.path.exists(settings_dir):
  os.makedirs(settings_dir)
instagram = Instagram(username, password, debug, IGDataPath=settings_dir)
#########

## Login
try:
  instagram.login()
except Exception as e:
  e.message
################

file_name = sys.argv[3]
message = sys.argv[4]

with open(file_name) as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for idx,username in enumerate(csvReader):
    username_id = instagram.getUsernameId(username[0])
    print(username_id)
    instagram.direct_message(str(username_id), message)

# For optimization:
# print("SELF USER FOLLOWERS")
# followers = instagram.getSelfUserFollowers()
# print(followers)
