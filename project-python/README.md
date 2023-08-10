## Data collection and preprocessing
###

### Prerequisites

1. Create an application on https://www.reddit.com/prefs/apps and save:
* client_id (below personal use script)
* client_secret (secred) 
* user_agent (app name)

2. In scraper.py replace client_id, client_secret, and user_agent with the ones of your app.

3. Create a virtual environment and install requirements

    python3.9 -m venv env
    . env/bin/activate
    pip install -r requirements.txt

4. Create a folder named data

###
### Collect reddit data

    python scraper.py


### Preprocess data

Extract emotional tone and emotions from posts and comments

    python preprocess.py
