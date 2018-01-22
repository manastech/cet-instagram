# -*- coding: utf-8 -*-
## Imports
from InstagramAPI import Instagram
from time import sleep
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

# Login
try:
  instagram.login()
except Exception as e:
  print(e)
################

file_name = sys.argv[3]
message_file = sys.argv[4]

with open(message_file) as message:
  message = message.read()
  # for line in message.readlines():
  # print("W")
  # print(line)

with open(file_name) as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for idx,username in enumerate(csvReader):
    if not username:
      continue
    username_id = instagram.getUsernameId(username[0])
    instagram.direct_message(str(username_id), message)
  sleep(2)

# For optimization:
# print("SELF USER FOLLOWERS")
# followers = instagram.getSelfUserFollowers()
# print(followers)
