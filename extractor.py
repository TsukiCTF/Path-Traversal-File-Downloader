import glob

class Extractor:
  def __init__(self, basedir):
    # set base directory which is a root directory of all files/directories to be processed
    self.basedir = basedir

  def extract(self):
    # get all files in base directory recursively
    all_files = glob.glob(self.basedir + "/**/*.*", recursive=True)
    for file_path in all_files:
      # extract wanted portion from file
      code = self.extract_from_file(file_path)
      # overwrite the file content with extracted text
      self.overwrite_file(file_path, code)

  def extract_from_file(self, file_path):
    lines = []
    with open(file_path, 'r') as f:
      lines = f.readlines()
    """ EVERY WEBSITE WITH A PATH TRAVERSAL VULNERABILITY WILL HAVE DIFFERENTLY STRUCTURED OUTPUT """
    """ THIS IS WHERE YOU WRITE YOUR OWN EXTRACTION LOGIC """
    """ FOR EXAMPLE, YOU CAN EXTRACT A PORTION OF PHP CODE FROM THE FILE """
    return ''.join(lines) # THIS LINE IS JUST A PLACEHOLDER
    
  def overwrite_file(self, file_path, content):
    with open(file_path, 'w') as f:
      f.write(content)
