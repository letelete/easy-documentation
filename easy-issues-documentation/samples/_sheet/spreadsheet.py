import pygsheets
import sched, time
from _utils import user_data
from oauth2client.service_account import ServiceAccountCredentials

class Sheet():

  def __init__(self, list_of_records):
    self.config = user_data.Config()
    self.list_of_records = list_of_records
    self.sheet = self._get_sheet()
    self.s = sched.scheduler(time.time, time.sleep)

  def _get_sheet(self):
    c = pygsheets.authorize(outh_file='./config/client_secret.json')
    sheet_name = self.config.get('sheet', 'name')
    sh = c.open(sheet_name)
    return sh.sheet1

  def create_table(self):
    self._create_header()
    self._insert_rows_into_sheet()

  def _create_header(self):
    self.sheet.clear()
    row_data = self.config.get('sheet', 'header_rows')
    self.sheet.update_cells('A1:D1', row_data)

  def _insert_rows_into_sheet(self):
    self.sheet.update_cells('A2', self.list_of_records)