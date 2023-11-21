import os
import pandas as pd
from supabase.client import create_client

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

filename = "sample.csv"

bucket_name: str = os.environ["SUPABASE_STORAGE_BUCKET"]

with open(filename, "wb+") as f:
    res = supabase.storage.from_(bucket_name).download("test.csv")
    f.write(res)

df = pd.read_csv(filename)

print(df.head())
