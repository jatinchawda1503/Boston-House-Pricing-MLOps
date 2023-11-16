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
    a. Go to https://github.com/username/project/settings/secrets/actions
    b. Click on new repository secret
    b. Add 
        i. HEROKU_API_KEY -> https://dashboard.heroku.com/account 
        ii. HEROKU_APP_NAME -> Heroku Project Name 
        iii. HEROKU_EMAIL -> Email Address

Push a new change then GitHub Action will Automatically start to deploy the application. 