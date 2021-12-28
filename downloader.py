import os
import re
import requests

class Downloader:
  def __init__(self, vulnerable_uri, location_file, path_to_save):
    # set Downloader properties
    self.vulnerable_uri = vulnerable_uri
    self.location_file = location_file  # file containing target locations with no URI
    self.path_to_save = path_to_save
    self.locations = [] # list containing target locations
    # load locations from location file
    self.load_locations()

  def load_locations(self):
    with open(self.location_file, 'r') as f:
      # add all locations into a list
      for location in f.readlines():
        location = location.strip() # remove whitespace (if there is)
        self.locations.append(location)

  def print_targets(self):
    # print all target URIs to be downloaded from
    for location in self.locations:
      uri = self.vulnerable_uri + location # concatenate base URI with location
      print(uri)

  def download(self):
    for location in self.locations:
      # check if location is inside a directory
      is_inside_dir = re.search('^.*\/.*$', location)
      if is_inside_dir:
        # get the directory name portion from location string
        dirname = '/'.join(location.split('/')[:-1])
        # create directory on disk before downloading the file
        self.create_directory(dirname)
      # download the file and save into the disk
      self.save_file(location)

  def create_directory(self, dirname):
    # prepend user chosen path on disk in which saved files will go
    if self.path_to_save != '':
      dirname = self.path_to_save.rstrip('/') + '/' + dirname
    # equivalent to "mkdir -p" in bash
    # this is useful when nested directory is passed, such as "/dir1/dir2"
    os.makedirs(dirname, exist_ok=True)

  def save_file(self, location):
    uri = self.vulnerable_uri + location # concatenate base URI with location
    # do GET request and fetch the content
    r = requests.get(uri)
    content = r.content
    # prepend user chosen path on disk in which saved files will go
    if self.path_to_save != '':
      location = self.path_to_save.rstrip('/') + '/' + location
    # save the content into a file on disk
    with open(location, 'wb') as f:
      f.write(content)
