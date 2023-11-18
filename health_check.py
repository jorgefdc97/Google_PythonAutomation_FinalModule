#!/usr/bin/env python3

import psutil, shutil
import socket
import emails
import os, sys

error = "Error"
#CPU usage is over 80
def cpu_check():
  cpu_usage = psutil.cpu_percent(1) 
  return not cpu_usage > 80

#available disk space is lower than 20%
def disc_space_check():  
  disk_usage = shutil.disk_usage("/")
  disk_total = disk_usage.total
  disk_free = disk_usage.used
  threshold = disk_free / disk_total * 100
  return threshold > 20

#available memory is less than 500MB
def available_memory_check():
  available = psutil.virtual_memory().available
  available_in_MB = available / 1024 ** 2 #convert to mb
  return available_in_MB > 500

#hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip == "127.0.0.1"

if not cpu_check():
  error = "Error - CPU usage is over 80%"

if not disc_space_check():
  error = "Error - Available disk space is less than 20%"

if not available_memory_check():
  error = "Error - Available memory is less than 500MB"

if not hostname_check():
  error = "Error - localhost cannot be resolved to 127.0.0.1"

emails.send_email_error(error)

