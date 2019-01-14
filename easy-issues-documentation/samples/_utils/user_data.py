import json

def get_json_data_from_path(path):
    with open(path) as f:
      data = json.load(f)
      return data

class Github_secret_key():
    def __init__(self):
        self.data = get_json_data_from_path('./config/github_secret_key.json')

    def get(self):
        return self.data['access_token']

class Config():
    def __init__(self):
        self.data = get_json_data_from_path('./config/config.json')

    def get(self, parent, *childs):
        return self.get_child_of(parent, childs)
    
    def get_child_of(self, parent, childs):
        root = self.data[parent]
        for c in childs:
            root = root[c]
        return root