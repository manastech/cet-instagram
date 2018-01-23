# -*- coding: utf-8 -*-
## Imports
from InstagramAPI import Instagram
from time import sleep
import csv
import sys
import os
import traceback
import re


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

with open(message_file) as message_file:
  message = message_file.read()
  urls = re.findall('(http[s]?:\/\/.+)\s', message)
  print("URLS")
  print(urls)
  message_list = [message]
  if len(message) > 1000:
    msg_count = len(message) / 1000
    message_list = message.split("\n")
    message_list = ["\n".join(message_list[0:len(message_list)//2]), "\n".join(message_list[len(message_list)//2+1:len(message_list)-1])]

failed_usernames = []
successful = 0
with open(file_name) as csvDataFile:
  csv_data = csv.reader(csvDataFile)

  for username in csv_data:
      if not username:
        continue
      try:
        username_id = instagram.getUsernameId(username[0])
        for message_part in message_list:
          sleep(5)
          instagram.direct_message(str(username_id), message_part)
        for url in urls:
          sleep(5)
          instagram.direct_message(str(username_id), url)
        successful += 1
      except Exception as err:
        failed_usernames.append(username[0])
        print(traceback.format_exc())


print("")
print("RESULTADOS: ")
print("Mensajes enviados con éxito: ", successful)
print("Usuarias a las que no se pudo enviar: ")
print(", ".join(failed_usernames))
