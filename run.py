#! /usr/bin/env python3

import os
import requests

server="http://34.125.205.88/fruits/"
path = "/home/student-02-7e2a3189f672/supplier-data/descriptions/"

for file in os.listdir(path):
  dict={}
  file_path = path + file
  with open(file_path, "r") as f:
    lines = f.readlines()
  dict["name"]=lines[0].strip("\n")
  dict["weight"]=lines[1].strip(" lbs\n")
  dict["description"]=lines[2].strip("\n")
  dict["image_name"]=file.strip("txt") + "jpeg"
  #print(dict)
  requests.post(server, json=dict)
