# -*- coding: utf-8 -*-
## Imports
from InstagramAPI import Instagram
from time import sleep
from math import ceil
import csv
import sys
import os
import traceback
import re

# Set up logger file
sys.stdout = open('instagram-messages-log.txt', 'a')
########

## Config data
username = sys.argv[1]
password = sys.argv[2]
debug = False

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
# ###############

# Message parameters
file_name = sys.argv[3]
message_file = sys.argv[4]
#########

# Parse message and divide in parts if necessary
with open(message_file) as message_file:
  message = message_file.read()
  urls = re.findall('(http[s]?:\/\/.+)\s', message)
  message_list = [message]
  if len(message) > 1000:
    msg_count = int(ceil(float(len(message)) / 1000))
    lines = message.split("\n")
    lines_per_message = int(ceil(float(len(lines)) / msg_count))
    message_list = []
    for i in range(0,msg_count):
      message_list.append("\n".join(lines[i*lines_per_message:(i+1)*lines_per_message]))
##########


failed_usernames = []
successful = 0
with open(file_name) as csvDataFile:
  csv_data = csv.reader(csvDataFile)

  for username in csv_data:
      if not username:
        continue
      try:
        sleep(10)
        username_id = instagram.getUsernameId(username[0])
        for message_part in message_list:
          sleep(3)
          instagram.direct_message(str(username_id), message_part)
        for url in urls:
          sleep(3)
          instagram.direct_message(str(username_id), url)
        successful += 1
      except Exception as err:
        failed_usernames.append(username[0])
        print(traceback.format_exc())


print >> sys.stderr, "RESULTADOS: "
print >> sys.stderr, "Mensajes enviados con éxito: ", successful
print >> sys.stderr, "Usuarias a las que no se pudo enviar: "
print >> sys.stderr, ", ".join(failed_usernames)
