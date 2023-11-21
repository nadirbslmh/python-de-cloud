import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd


def extract(filename):
    df = pd.read_csv(filename)
    return df


def transform(df):
    # drop duplicates
    df = df.drop_duplicates()
    # format phone numbers
    df["Phone Number"] = df["Phone Number"].str.replace("-", "")
    df["Phone Number"] = df["Phone Number"].apply(lambda x: "+62" + x)
    # get data with reason not equals null
    df = df[df["Reason"] != "-"]
    # reset index
    df = df.reset_index(drop=True)

    return df


def load(df):
    cred = credentials.Certificate("/home/nadir/codes/python-de-cloud/accountKey.json")

    storage_bucket = os.environ["GOOGLE_STORAGE_BUCKET"]

    firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

    bucket = storage.bucket()

    filename = "survey.parquet"

    df.to_parquet(filename)

    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

    print("load success")


# perform ETL
df = extract("survey_data.csv")
df_result = transform(df)
load(df_result)
