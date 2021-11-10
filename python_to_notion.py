import requests, json
import datetime
from dateutil.relativedelta import relativedelta

today = datetime.datetime.now()
today_convert = today.strftime("%Y-%m-%dT%H:%M+09:00")
pro_name = "전기구이 통닭"

#설정
token = 'secret_nseqnEbZWiM1dPJyrWqX1neTEOnGcdobO5d6xQI1Wnt'
id_database = 'bc4349b14ba04fa1a4cd76c35213f844'
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}
def readDatabase(id_database, headers):
    readURL = f"https://api.notion.com/v1/databases/{id_database}/query"
    res = requests.request("POST", readURL, headers=headers)
    data = res.json()
    # print(res.status_code)
    # print(res.text)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

def createDatabase(id_database, headers):
    createURL = 'https://api.notion.com/v1/pages'
    newPageData = {
    "parent": {"database_id": id_database},
    "properties": {
        "홀딩 타임": {"date": {"start": today_convert}},
        "상품명": {"title": [{"text": {"content": pro_name}}]},
        "보관법": {"select": {"name": "냉장"}}
                }
            }

    data = json.dumps(newPageData)
    res = requests.request("POST", createURL, headers=headers, data=data)
    print(res.status_code)

# 실행!
readDatabase(id_database, headers)
# createDatabase(id_database, headers)
