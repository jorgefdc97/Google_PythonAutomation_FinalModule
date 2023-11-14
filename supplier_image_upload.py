#!/usr/bin/env python3

import requests
from os import listdir
import re 

url = "http://localhost/upload/"
for file in listdir("/home/student-02-7e2a3189f672/supplier-data/images"):
  if (re.search(r"[0-9]\.jpeg", file) != None):
    file_path = "/home/student-02-7e2a3189f672/supplier-data/images/" + file 
    with open(file_path, "rb") as opened:
      request = requests.post(url, files={"file": opened})
