from github import Github
from _utils import user_data

API_RESOURCE_CHANGES_REQUESTED = 'CHANGES_REQUESTED'
API_RESOURCE_CHANGES_APPROVED = 'APPROVED'

class Data():
  def __init__(self, current_pr):
    self.current_pr = current_pr
    self.config = user_data.Config()

  def get_url(self):
    return self.current_pr.html_url

  def get_status(self):
    reviews = self.current_pr.get_reviews()
    if self._does_contains_reviews(reviews):
      if self._is_pr_mergable():
        return self._get_reviews_state(reviews)
      else:
        return self.config.get('status', 'changes_needed')
    else:
      return self.config.get('status', 'not_reviewed')

  def _does_contains_reviews(self, reviews):
    return reviews.totalCount > 0

  def _is_pr_mergable(self):
    return self.current_pr.mergeable

  def _get_reviews_state(self, reviews):

    """

    We are reversing the list to make reviews search search more efficient and much more accurate.
    Mostly the API_RESOURCE_CHANGES_APPROVED rather appears as the last review comment
    than the first one f(ಠ‿↼)z

    """

    for r in reviews.reversed:
      if r.state == API_RESOURCE_CHANGES_APPROVED:
        break
      elif r.state == API_RESOURCE_CHANGES_REQUESTED:
        return self.config.get('status', 'changes_needed')
    return self.config.get('status', 'ready_to_merge')

  def get_title(self):
    return self.current_pr.title
