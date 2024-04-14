import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pandas as pd


class CoffeeETL:
    def __init__(self, cert_path: str, storage_bucket: str) -> None:
        self.__cert_path = cert_path
        self.__storage_bucket = storage_bucket

    def extract_from_storage(self) -> pd.DataFrame:
        try:
            cred = credentials.Certificate(self.__cert_path)

            storage_bucket = self.__storage_bucket

            firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

            bucket = storage.bucket()

            filename = "coffee_shop.csv"

            blob = bucket.get_blob("coffee_shop.csv")

            with blob.open(mode="r") as file:
                df = pd.read_csv(file)

            return df
        except Exception as e:
            print(f"An error occurred when extracting data: ${e}")
            return pd.DataFrame()

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[(df["menu"] != "green tea") & (df["menu"] != "jasmine tea")]
        df = df.reset_index(drop=True)
        return df

    def load(self, df: pd.DataFrame) -> None:
        try:
            df.to_csv("coffee_data.csv")
            print("data loaded successfully!")
        except Exception as e:
            print(f"An error occurred when loading data: ${e}")
