import os
import firebase_admin

from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("/home/nadir/codes/python-de-cloud/accountKey.json")

storage_bucket = os.environ["GOOGLE_STORAGE_BUCKET"]

firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

bucket = storage.bucket()

blob = bucket.get_blob("coffee_shop.csv")

blob.download_to_filename(filename="coffee_tx.csv")
