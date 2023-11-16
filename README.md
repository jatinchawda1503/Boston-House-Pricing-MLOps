# Boston-House-Pricing-MLOps

 
## Environment Creation
```
conda create -n boston-pricing-mlops python=3.11
conda activate boston-pricing-mlops
```
## Offline Run
### Install the dependency 

```
pip install -r requirements.txt
```

### Run Flask App 

```
cd app
python app.py
```

## Heroku Deployment

1. Clone the Repo
2. Setup the Heroku Account
3. Create New App 
5. Add Github Acoount followed by Cloned Branch
4. Add the Heroku API key, Project Name and Email id to GitHub Actions. 
    1. Go to https://github.com/username/project/settings/secrets/actions
    2. Click on new repository secret
    3. Add the following Keys
        1. HEROKU_API_KEY -> https://dashboard.heroku.com/account 
        2. HEROKU_APP_NAME -> Heroku Project Name 
        3. HEROKU_EMAIL -> Email Address

Push a new change then GitHub Action will automatically start to deploy the application. 