import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd

cred = credentials.Certificate("/home/nadir/codes/python-de-cloud/accountKey.json")

storage_bucket = os.environ["GOOGLE_STORAGE_BUCKET"]

firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

bucket = storage.bucket()

blob = bucket.get_blob("coffee_shop.csv")

with blob.open(mode="r") as file:
    df = pd.read_csv(file)

print(df.head())
