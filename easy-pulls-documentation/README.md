<h1 align="center"><a href="" alt="GitHub release"><img src="https://i.imgur.com/VjWsVok.gif" /></a></h1>
<h2 align="center"><b>Easy Pulls Documentation</b></h2>
<h4 align="center">Python script to create a documentation for pull requests status in repository. Made for Google Code-In 2018</h4>

### Live preview

You can check this script in action [here](https://docs.google.com/spreadsheets/d/1JZMVIAeHUEAk836dd1pxCAU5NJKmGBG5yfy7j-zq38Y/edit?ouid=103369938868471431746&usp=sheets_home&ths=true). It's hosted on Heroku and updated every 5 min.

### How does it works

Script creates a repository documentation by checking if the PR has been reviewed by someone

#### Status meanings

* Ready to be merged - It has been reviewed, and no change has been asked by the reviewer / Requested changes were accepted
* Changes Needed - If it has been reviewed, and some change has been asked by the reviewer
* NEED REVIEW - If it has not been reviewed

---

### How to use

#### Initial setup

* Clone this repo on your machine
* Make sure you have [Python](https://www.python.org/downloads) and [PIP](https://pypi.org/project/pip/) installed
* Install required packages with pip
  * open your terminal
  * type `pip install pygsheets oauth2client PyGithub beautifulsoup4 requests halo`

#### Authorizing pygsheets

To make use of google's spreadsheets, you need to create your own google app which will access to your shared google's sheet

* ([Here's how](https://www.youtube.com/watch?v=vISRn5qFrkM))
* when your google app is ready, and credentials added to project, you should have your OAuth client ID `.json` file saved on your machine.
  * rename your .json file to `client_secret.json`
  * move your client_secret.json to `./config` directory
  
#### github access token

To make use of github api, you'll need to configure your github token

* create [github access token](https://github.com/settings/tokens)
* move to the `./config` directory
* create `github_secret_key.json`
* paste these lines into your .json file, and change github token to yours
  
```
{
  "access_token" : "REPLACE_THIS_TEXT_WITH_YOURS_TOKEN"
}
```

#### customize sheet, set github repo

* configure your settings in `./config/config.json` file

__NOTICE__: 

* Don't add/remove headers since these are kinda hard typed into code. You can only rename them.

#### Running script

* run script by:
  * typing `py ./samples/main.py` in your terminal




