from github import Github
from _utils import user_data
from _git import pr_reference_scrapper

class Data():
  def __init__(self, current_issue, repo):
    self.current_issue = current_issue
    self.repo = repo
    self.config = user_data.Config()

  def get_url(self):
    return self.current_issue.html_url

  def get_title(self):
    return self.current_issue.title

  def get_status(self):
    return self._get_issue_status()

  def _get_issue_status(self):
    url = self.get_url()
    all_pr_ids = pr_reference_scrapper.get_references_ids(url)

    if all_pr_ids is None or len(all_pr_ids) <= 0:
      return 'open'
    elif self._are_all_pr_ids_similiar(all_pr_ids):
      pr_id = all_pr_ids[0]
      return self._get_pr_state(pr_id)
    else:
      return self._handle_multiple_prs(all_pr_ids)

  def _are_all_pr_ids_similiar(self, all_pr_ids):
    if len(all_pr_ids) > 1:
      for n, pr_id in enumerate(all_pr_ids):
        if n > 0 and pr_id != all_pr_ids[n-1]:
          return False

  def _handle_multiple_prs(self, all_pr_ids):
    state = 'open'
    for pr_amount in range(len(all_pr_ids)-1, -1, -1):
      pr = all_pr_ids[pr_amount]
      state = self._get_pr_state(pr)
      if state == 'closed':
        return state

    return 'multiple_prs'

  def _get_pr_state(self, pr_id):
    try:
      pull_request = self.repo.get_pull(pr_id)
      if pull_request.is_merged():
        return 'closed'
      elif pull_request.state == 'closed':
        return 'open'
      else:
        return 'in_progress'
    except Exception as e:
      print("Error", e)
      return 'error | pr_id: {}'.format(pr_id)

    return True