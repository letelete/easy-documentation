from _sheet import spreadsheet
from _git import github_client
from halo import Halo

class Main():
  def __init__(self):
    pass

  def easy_pulls_documentation(self):
    spinner = Halo(text='Initializing GitHub client', text_color= 'green', color='magenta', spinner='dots')
    try:
      spinner.start()
      self._initialize_github_client()
      
      if self.git != None:
        spinner.succeed()

        spinner.start("Fetching pull requests data")
        self._load_records()
        spinner.succeed()

        spinner.start("Initializing Google sheet")
        self._initialize_google_spreadsheet()
        spinner.succeed()

        spinner.start("Creating a sheet and inserting records")
        self._create_table_and_insert_records()
        spinner.succeed()

      else:
        spinner.fail()

    except (SystemExit):
      spinner.stop()
    
  def _initialize_github_client(self):
    self.git = github_client.Git()

  def _load_records(self):
    self.records = self.git.get_pulls_records()

  def _initialize_google_spreadsheet(self):
    self.sheet = spreadsheet.Sheet(self.records)

  def _create_table_and_insert_records(self):
    self.sheet.create_table()

main = Main()
main.easy_pulls_documentation()