<h1 align="center"><a href="" alt="GitHub release"><img src="https://i.imgur.com/i9L0E4Z.gif" /></a></h1>>
<h2 align="center"><b>Easy Issues Documentation</b></h2>
<h4 align="center">Python script to create a documentation for issues status in repository. Made for Google Code-In 2018</h4>

### Live preview

You can check this script in action [here](https://docs.google.com/spreadsheets/d/1sysJ09YMN4m8Ex1ZufGfm3iMadkIIX8SKPXPHIlJaAY/edit?usp=sharing). It's hosted on Heroku and updates every 5 min.

### How does it works

Script creates a repository documentation by checking if the issue has any pull-request references.

#### Status meanings

* open - Means there are no pull request references to this task. It's open so its ready to claim, or someone's just already claimed it, but didn't send a solution yet. It might also happened when someone send an issue's solution but its got closed and not merged.
* in_progress - Means that someone already send a solution for the issue and its waiting for merge.
* closed - Means that someone's solution got merged, so the task can be closed
* multiple_prs - Means there are many unique pull request for single issue and these are all open, or just script struggling with recognise if issue got resolved with so many prs.

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

* If you really want to colorize issue statuses you can enable it in your config.json file. It works really slowly, so I don't recommend that. It's better to set a conditional formatting in your spreadsheet for status column.

#### Running script

* run script by:
  * typing `py ./samples/main.py` in your terminal




