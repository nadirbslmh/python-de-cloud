# === Example 1 ===
# import os
# from reqres_etl import ReqresETL

# etl = ReqresETL(
#     base_url="https://reqres.in/api/users",
#     cert_path="/home/nadir/codes/python-de-cloud/accountKey.json",
#     storage_bucket=os.environ["GOOGLE_STORAGE_BUCKET"],
# )

# result = etl.extract_from_api()
# df = etl.transform(result)
# etl.load(df)
# === Example 1 ===

# === Example 2 ===
# import os
# from coffee_etl import CoffeeETL

# etl = CoffeeETL(
#     cert_path="/home/nadir/codes/python-de-cloud/accountKey.json",
#     storage_bucket=os.environ["GOOGLE_STORAGE_BUCKET"],
# )

# result = etl.extract_from_storage()
# df = etl.transform(result)
# etl.load(df)
# === Example 2 ===

# === Example 3 ===
# import os
# from tenders_etl import TendersETL

# etl = TendersETL(
#     base_url="https://tenders.guru/api/es/tenders",
#     supabase_url=os.environ["SUPABASE_URL"],
#     supabase_key=os.environ["SUPABASE_KEY"],
#     supabase_storage_bucket=os.environ["SUPABASE_STORAGE_BUCKET"],
# )

# result = etl.extract_from_api()
# df = etl.transform(result)
# etl.load(df)
# === Example 3 ===
