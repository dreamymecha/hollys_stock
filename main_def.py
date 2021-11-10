# 할리스 재고 관리 프로그램
# 베이커리는 더 이상 해동시키지 않아도 되는 듯

# 할리스 재고 관리 프로그램
# 베이커리는 더 이상 해동시키지 않아도 되는 듯

import requests, json
import time
import datetime
from dateutil.relativedelta import relativedelta

# 변수 설정
pro_name = None
method = None
crit = None
exp = None
defro_start = None
defro_end = None
open_date = None
hold_time = None

# 노션 Setting
token = 'secret_nseqnEbZWiM1dPJyrWqX1neTEOnGcdobO5d6xQI1Wnt'
id_database = 'bc4349b14ba04fa1a4cd76c35213f844'
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

code = int(input("제품 코드 입력(1 ~ ?): "))

# 실질적인 데이터 섹션
if code == 1:
    pro_name = "플레인 얼음"
    method = "냉동"
    crit = input("제조일?(예: 2021-05-05)?: ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=3)).strftime("%Y-%m-%d")
    hold_time = exp

if code == 2:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "밀크베이스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "밀크베이스"
        hold_time = exp

if code == 3:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "빙수용 애플망고 베이스(드리즐통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
            hold_crit = today + datetime.timedelta(days=7)
            hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
        if div == 2:
            pro_name = "빙수용 애플망고 베이스(개봉)"
            today = datetime.datetime.now()
            open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
            hold_crit = today + datetime.timedelta(days=30)
            hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "빙수용 애플망고 베이스"
        hold_time = exp

if code == 4:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "복숭아 베이스(드리즐통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
            hold_crit = today + datetime.timedelta(days=7)
            hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
        if div == 2:
            pro_name = "복숭아 베이스(개봉)"
            today = datetime.datetime.now()
            open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
            hold_crit = today + datetime.timedelta(days=30)
            hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "복숭아 베이스"
        hold_time = exp

if code == 5:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "단팥(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_crit = today + datetime.timedelta(days=5)
        hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "단팥"
        hold_time = exp

if code == 6:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "19곡물파우더(토핑통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
            hold_crit = today + datetime.timedelta(hours=72)
            hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
        if div == 2:
            pro_name = "19곡물파우더(개봉)"
            hold_time = exp
    if open == 2:
        pro_name = "19곡물파우더"
        hold_time = exp

if code == 7:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "빙수떡(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + relativedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "빙수떡"
        method = "냉동"
        hold_time = exp

if code == 8:
    method = "실온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "그래놀라믹스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "그래놀라믹스"
        hold_time = exp

if code == 9:
    method = "냉동"
    pro_name = "냉동딸기다이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 10:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "백도 통조림(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "백도 통조림"
        hold_time = exp

if code == 11:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "화이트펄(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "화이트펄"
        hold_time = exp

if code == 12:
    method = "상온"
    pro_name = "딸기파우더"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 13:
    method = "냉동"
    pro_name = "냉동망고슬라이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 14:
    method = "상온"
    pro_name = "코코넛 슬라이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 15:
    method = "냉동"
    pro_name = "애플망고 아이스크림"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 16:
    method = "냉동"
    div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
    if div == 1:
        pro_name = "요거트 아이스크림(소분)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
    if div == 2:
        pro_name = "요거트 아이스크림"

if code == 17:
    method = "실온"
    pro_name = "나뭇잎코인"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 18:
    method = "실온"
    pro_name = "장식용 초코코인"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 19:
    method = "냉동"
    pro_name = "크로플"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 20:
    method = "냉동"
    pro_name = "크림치즈 비스켓"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 21:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + datetime.timedelta(weeks=5)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "디카페인 커피 원액(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=72)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "디카페인 커피 원액"
        hold_time = exp

if code == 22:
    method = "냉동"
    pro_name = "애플망고 스무디"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 23:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "애플망고 베이스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=20)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "애플망고 베이스"
        hold_time = exp

if code == 24:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
    if defro == 1:
        pro_name = "오렌지 당근 착즙주스(냉장 해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "오렌지 당근 착즙주스"
        method = "냉동"
        hold_time = exp

if code == 25:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
    if defro == 1:
        pro_name = "사과 비트 착즙주스(냉장 해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "사과 비트 착즙주스"
        method = "냉동"
        hold_time = exp

if code == 26:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "애플망고 다이스(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=6) + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "애플망고 다이스"
        method = "냉동"
        hold_time = exp

if code == 27:
    method = "냉동"
    pro_name = "크로플"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 28:
    method = "상온"
    pro_name = "슈가파우더"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")

if code == 29:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "마스카포네 티라미스(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "마스카포네 티라미스"
        method = "냉동"
        hold_time = exp

if code == 30:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "쿠키&치즈(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "쿠키&치즈"
        method = "냉동"
        hold_time = exp

if code == 31:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "뉴욕 치즈(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "뉴욕 치즈"
        method = "냉동"
        hold_time = exp

if code == 32:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "리얼 벨지안 초코(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "리얼 벨지안 초코"
        method = "냉동"
        hold_time = exp

if code == 33:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "딸기 생크림(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "딸기 생크림"
        method = "냉동"
        hold_time = exp

if code == 34:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "블루베리 치즈 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "블루베리 치즈 라운드"
        method = "냉동"
        hold_time = exp

if code == 35:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "초코벨벳 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "초코벨벳 라운드"
        method = "냉동"
        hold_time = exp

if code == 36:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "티라미스 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "티라미스 라운드"
        method = "냉동"
        hold_time = exp

if code == 37:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "표곰이 하우스(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "표곰이 하우스"
        method = "냉동"
        hold_time = exp

if code == 38:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "산딸기 빅카롱(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "산딸기 빅카롱"
        method = "냉동"
        hold_time = exp

if code == 39:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "초코 빅카롱(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "초코 빅카롱"
        method = "냉동"
        hold_time = exp

if code == 40:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "뉴 크로크무슈(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "뉴 크로크무슈"
        method = "냉동"
        hold_time = exp

if code == 41:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "페스토 햄 모짜렐라 샌드위치(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "페스토 햄 모짜렐라 샌드위치"
        method = "냉동"
        hold_time = exp

if code == 42:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "올리브 베이컨 치아바타 샌드위치(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "올리브 베이컨 치아바타"
        method = "냉동"
        hold_time = exp

if code == 43:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "미트볼 칠리 치즈 샌드위치(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "미트볼 칠리 치즈 샌드위치"
        metho = "냉동"
        hold_time = exp

if code == 44:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "샌드위치 식빵(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "샌드위치 식빵"
        metho = "냉동"
        hold_time = exp

if code == 45:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "오곡 식빵(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "오곡 식빵"
        metho = "냉동"
        hold_time = exp

if code == 46:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "뿌셔먹는 에그샐러드(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=2)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "뿌셔먹는 에그샐러드"
        hold_time = exp

# 이 부분에 대해서는 논의 요망
if code == 47:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(days=3)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "뿌셔먹는 에그샐러드(으깬 거, 개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=2)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "뿌셔먹는 에그샐러드(으깬 거)"
        hold_time = exp

if code == 48:
    method = "냉장"
    pro_name = "에그마요"
    today = datetime.datetime.now()
    hold_time = (today + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")

if code == 49:
    method = "냉장"
    pro_name = "반반마요"
    today = datetime.datetime.now()
    hold_time = (today + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")

if code == 50:
    pro_name = "사라다 샐러드"
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05)?: ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(days=40)).strftime("%Y-%m-%d")
    hold_time = exp

if code == 51:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "바삭불고기 & 트리플치즈치킨(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "바삭불고기 & 트리플치즈치킨"
        metho = "냉동"
        hold_time = exp

if code == 52:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "매콤닭갈비 & 바베큐포크(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "매콤닭갈비 & 바베큐포크"
        metho = "냉동"
        hold_time = exp

if code == 53:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "베이컨 에그데니쉬(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "베이컨 에그데니쉬"
        metho = "냉동"
        hold_time = exp

if code == 54:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "스위트콘 에그데니쉬(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
        defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
    if defro == 2:
        pro_name = "스위트콘 에그데니쉬"
        metho = "냉동"
        hold_time = exp

if code == 76:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + datetime.timedelta(weeks=5)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "콜드브루 원액(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(hours=72)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "콜드브루 원액"

# 커피의 개봉 여부는 어떻게 판단을 할지?
if code == 77:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "에스프레소 로스트(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "에스프레소 로스트"

if code == 78:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "프리미엄 블렌드(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "프리미엄 블렌드"

if code == 79:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "메뉴 제조용 MD 커피(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "메뉴 제조용 MD 커피"

if code == 80:
    method = "냉장"
    pro_name = "일반 우유"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + datetime.timedelta(days=14)

if code == 81:
    method = "냉장"
    pro_name = "저지방 우유"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + datetime.timedelta(days=12)

if code == 82:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = (datetime.date(y, m, d) + relativedelta(months=8) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "스프레이형 휘핑기(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
        hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
    if open == 2:
        pro_name = "스프레이형 휘핑기"
        hold_time = exp

# 노션 작동
createURL = 'https://api.notion.com/v1/pages'
if defro_start == None:
    if exp == None:
        if hold_time == None:
            newPageData = {
            "parent": {"database_id": id_database},
            "properties": {
                "상품명": {"title": [{"text": {"content": pro_name}}]},
                "보관법": {"select": {"name": method}}
                }
            }
        else:
            newPageData = {
                "parent": {"database_id": id_database},
                "properties": {
                    "상품명": {"title": [{"text": {"content": pro_name}}]},
                    "보관법": {"select": {"name": method}},
                    "홀딩 타임": {"date": {"start": hold_time}}
                }
            }
    else:
        if open_date == None:
            newPageData = {
                "parent": {"database_id": id_database},
                "properties": {
                    "유통기한": {"date": {"start": exp}},
                    "홀딩 타임": {"date": {"start": hold_time}},
                    "상품명": {"title": [{"text": {"content": pro_name}}]},
                    "보관법": {"select": {"name": method}}
                }
            }
        else:
            newPageData = {
                "parent": {"database_id": id_database},
                "properties": {
                    "유통기한": {"date": {"start": exp}},
                    "개봉일": {"date": {"start": open_date}},
                    "홀딩 타임": {"date": {"start": hold_time}},
                    "상품명": {"title": [{"text": {"content": pro_name}}]},
                    "보관법": {"select": {"name": method}}
                }
            }
else:
    newPageData = {
        "parent": {"database_id": id_database},
        "properties": {
            "유통기한": {"date": {"start": exp}},
            "해동 시작 시간": {"date": {"start": defro_start}},
            "해동 종료 시간": {"date": {"start": defro_end}},
            "홀딩 타임": {"date": {"start": hold_time}},
            "상품명": {"title": [{"text": {"content": pro_name}}]},
            "보관법": {"select": {"name": method}}
        }
    }

data = json.dumps(newPageData)
res = requests.request("POST", createURL, headers=headers, data=data)

if res.status_code == 200:
    print("기록 성공")
else:
    print("기록 실패...")
print("결과:", pro_name, method, exp, open_date, defro_start, defro_end, hold_time)