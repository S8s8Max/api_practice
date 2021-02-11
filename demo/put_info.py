import base64
import json
import urllib.request
import pandas as pd


# pandas processing
path = "/Users/kippeiwatanabe/Desktop/CodingSpace/practice/Python/api/api_practice/LendingInterestRate.csv"
df = pd.read_csv(path)

for row in df.iterrows():
    for i in range(1980,2021):
        year = i
        country = row[1][0]
        l_interest_rate = row[1][f"{i}"]

        # 変数は必要に応じて外部化してください。
        # api request
        url = "http://localhost:8000/api/logs/"
        method = "POST"
        headers = {"Content-Type": "application/json",}
        user = "S8s8Max"
        password = "perfume215"

        # PythonオブジェクトをJSONに変換する
        obj = {"year": year, "country": country, "l_interest_rate": l_interest_rate, }
        json_data = json.dumps(obj).encode("utf-8")

        credentials = ('%s:%s' % (user, password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))

        # httpリクエストを準備してPOST
        request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
        request.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
