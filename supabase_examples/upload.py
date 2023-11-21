import os
from supabase.client import create_client

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]
supabase = create_client(url, key)

bucket_name: str = os.environ["SUPABASE_STORAGE_BUCKET"]

with open("test.csv", "rb") as f:
    supabase.storage.from_(bucket_name).upload(
        file=f,
        path="test.csv",
    )
