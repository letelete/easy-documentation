import datetime
from github import Github
from _utils import user_data
from _git import pull

class Git:
  def __init__(self):
    self.config = user_data.Config()
    self.github_secret_key = user_data.Github_secret_key()

    try:
      access_token = self.github_secret_key.get()
      self.git = Github(access_token)
      self.repo = self._get_repository(self.git)
    except Exception as e:
      print('Errror:', e)

  def _get_repository(self, git):
    repo_name = self.config.get('repo', 'name')
    return git.get_repo(repo_name)

  def get_pulls_records(self):
    issues_records = []

    prs = self.repo.get_pulls(state='open')
    for pr in prs:
      self.pull_data = pull.Data(pr)
      record = [
        self._get_url(),
        self._get_title(),
        self._get_status(),
        self._get_formatted_date()
      ]
      issues_records.append(record)

    return issues_records

  def _get_url(self):
    return self.pull_data.get_url()

  def _get_title(self):
    return self.pull_data.get_title()

  def _get_status(self):
    return self.pull_data.get_status()

  def _get_formatted_date(self):
    dt = datetime.datetime.now()
    return '{}:{}'.format(dt.strftime('%H'), dt.strftime('%M'))
    