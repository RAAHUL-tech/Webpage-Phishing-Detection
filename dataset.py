import kaggle
import pandas as pd
import os

def extract_data():
    if not os.path.exists("data"):
        os.mkdir("data")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('danielfernandon/web-page-phishing-dataset',
                                      path='./data', unzip=True)
    print("Extracted data from source successfully!")
    df = pd.read_csv('./data/web-page-phishing.csv')
    train_data = df.iloc[:70000]
    test_data = df.iloc[70000:]
    train_data.to_csv("data/train.csv", index=False)
    test_data.to_csv("data/test.csv", index=False)
    print("Stored Training and testing data successfully!")

if __name__ == "__main__":
    extract_data()
