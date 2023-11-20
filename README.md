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
4. Add Github Account followed by Cloned Branch
5. Add the Heroku API key, Project Name, and Email id to GitHub Actions. 
    1. Go to https://github.com/username/project/settings/secrets/actions
    2. Click on "New repository secret"
    3. Add the following Keys:
        - HEROKU_API_KEY -> [Heroku API Key](https://dashboard.heroku.com/account)
        - HEROKU_APP_NAME -> Heroku Project Name 
        - HEROKU_EMAIL -> Email Address

Push a new change to trigger the GitHub Action deployment:

1. Make the necessary changes to your code.
2. Stage the changes:
    ```bash
    git add .
    ```
3. Commit the changes:
    ```bash
    git commit -m "Update code"
    ```
4. Push the changes to the remote repository:
    ```bash
    git push
    ```
5. GitHub Action will automatically start to deploy the application.

