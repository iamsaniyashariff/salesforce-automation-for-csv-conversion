import pandas as pd
from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

sf_username = os.getenv("username")
sf_password = os.getenv("password")
sf_securitytoken = os.getenv("security_token")


sf = Salesforce(username=sf_username, password=sf_password, security_token=sf_securitytoken)

query_accounts = "SELECT Id, Name, Type, Industry FROM Account"
accounts = sf.query_all(query_accounts)

accounts_df = pd.DataFrame(accounts['records']).drop(columns='attributes')
accounts_df.to_csv('accounts_data.csv', index = False)
print('Account data saved to accounts_data.csv')

query_contacts = "SELECT Id, FirstName, LastName, Email, AccountId FROM Contact"
contacts = sf.query_all(query_contacts)

contacts_df = pd.DataFrame(contacts['records']).drop(columns='attributes')
contacts_df.to_csv('contacts_data.csv', index=False)
print('Contact data saved.')
