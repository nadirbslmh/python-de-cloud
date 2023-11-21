import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd

cred = credentials.Certificate("/home/nadir/codes/python-de-cloud/accountKey.json")

storage_bucket = os.environ["GOOGLE_STORAGE_BUCKET"]

firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

bucket = storage.bucket()

df = pd.read_csv("test.csv")
df.to_parquet("test.parquet")

blob = bucket.blob("test.parquet")

blob.upload_from_filename("test.parquet")
