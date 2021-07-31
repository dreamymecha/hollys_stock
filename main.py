# 할리스 재고 관리 프로그램
# 베이커리는 더 이상 해동시키지 않아도 되는 듯

import pandas as pd
import sqlite3 as sql
import time
import datetime
from dateutil.relativedelta import relativedelta
import openpyxl

# connect = sql.connect("C:/Users/komes/Desktop/박지수의 문서/일/할리스/재고 관리 프로그램/database.db")
# 변수 설정
pro_name = None
method = None
crit = None
exp = None
defro_start = None
defro_end = None
open_date = None
hold_time = None

code = int(input("제품 코드 입력(1 ~ ?): "))

if code == 1:
    pro_name = "플레인 얼음"
    method = "냉동"
    crit = input("제조일?(예: 2021-05-05)?: ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=3)

if code == 2:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=2) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "밀크베이스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "밀크베이스"

if code == 3:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "빙수용 애플망고 베이스(드리즐통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime('%Y-%m-%d %H:%M')
            hold_crit = today + datetime.timedelta(days=7)
            hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
        if div == 2:
            pro_name = "빙수용 애플망고 베이스(개봉)"
            today = datetime.datetime.now()
            open_date = today.strftime('%Y-%m-%d %H:%M')
            hold_crit = today + datetime.timedelta(days=30)
            hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "빙수용 애플망고 베이스"

if code == 4:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "복숭아 베이스(드리즐통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime('%Y-%m-%d %H:%M')
            hold_crit = today + datetime.timedelta(days=7)
            hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
        if div == 2:
            pro_name = "복숭아 베이스(개봉)"
            today = datetime.datetime.now()
            open_date = today.strftime('%Y-%m-%d %H:%M')
            hold_crit = today + datetime.timedelta(days=30)
            hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "복숭아 베이스"

if code == 5:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "단팥(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_crit = today + datetime.timedelta(days=5)
        hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "단팥"

if code == 6:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
        if div == 1:
            pro_name = "19곡물파우더(토핑통 소분)"
            today = datetime.datetime.now()
            open_date = today.strftime('%Y-%m-%d %H:%M')
            hold_crit = today + datetime.timedelta(hours=72)
            hold_time = hold_crit.strftime('%Y-%m-%d %H:%M')
        if div == 2:
            pro_name = "19곡물파우더(개봉)"
    if open == 2:
        pro_name = "19곡물파우더"

if code == 7:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "빙수떡(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + relativedelta(days=7)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "빙수떡"
        method = "냉동"

if code == 8:
    method = "실온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "그래놀라믹스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "그래놀라믹스"

if code == 9:
    method = "냉동"
    pro_name = "냉동딸기다이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)

if code == 10:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "백도 통조림(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "백도 통조림"

if code == 11:
    method = "상온"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "화이트펄(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=10)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "화이트펄"

if code == 12:
    method = "상온"
    pro_name = "딸기파우더"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)

if code == 13:
    method = "냉동"
    pro_name = "냉동망고슬라이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)

if code == 14:
    method = "상온"
    pro_name = "코코넛 슬라이스"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)

if code == 15:
    method = "냉동"
    pro_name = "애플망고 아이스크림"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)

if code == 16:
    method = "냉동"
    div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
    if div == 1:
        pro_name = "요거트 아이스크림(소분)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M')
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
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)

if code == 18:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "표곰이 하우스(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "표곰이 하우스"
        method = "냉동"

if code == 19:
    method = "실온"
    pro_name = "장식용 초코코인"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)

if code == 20:
    method = "냉동"
    pro_name = "크로플"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)

if code == 21:
    method = "냉동"
    pro_name = "크림치즈 비스켓"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)

if code == 22:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + datetime.timedelta(weeks=5)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "디카페인 커피 원액(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=72)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "디카페인 커피 원액"

if code == 23:
    method = "냉동"
    pro_name = "애플망고 스무디"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)

if code == 24:
    method = "냉장"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "애플망고 베이스(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=20)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "애플망고 베이스"

if code == 25:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
    if defro == 1:
        pro_name = "오렌지 당근 착즙주스(냉장 해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=12)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "오렌지 당근 착즙주스"
        method = "냉동"

if code == 26:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
    if defro == 1:
        pro_name = "사과 비트 착즙주스(냉장 해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=12)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "사과 비트 착즙주스"
        method = "냉동"

if code == 27:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "애플망고 다이스(해동)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=6)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=6) + datetime.timedelta(hours=36)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "애플망고 다이스"
        method = "냉동"

if code == 28:
    method = "상온"
    pro_name = "슈가파우더"
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)

if code == 29:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "마스카포네 티라미스(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "마스카포네 티라미스"
        method = "냉동"

if code == 30:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "쿠키&치즈(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "쿠키&치즈"
        method = "냉동"

if code == 31:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "뉴욕 치즈(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "뉴욕 치즈"
        method = "냉동"

if code == 32:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "리얼 벨지안 초코(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "리얼 벨지안 초코"
        method = "냉동"

if code == 33:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "딸기 생크림(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "딸기 생크림"
        method = "냉동"

if code == 34:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "블루베리 치즈 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "블루베리 치즈 라운드"
        method = "냉동"

if code == 35:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "초코벨벳 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "초코벨벳 라운드"
        method = "냉동"

if code == 36:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "티라미스 라운드(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "티라미스 라운드"
        method = "냉동"

if code == 37:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "표곰이 하우스(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=4)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "표곰이 하우스"
        method = "냉동"

if code == 38:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "산딸기 빅카롱(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "산딸기 빅카롱"
        method = "냉동"

if code == 39:
    crit = input("제조일?(예: 2021-05-05): ")
    crit_split = crit.split('-')
    y = int(crit_split[0])
    m = int(crit_split[1])
    d = int(crit_split[2])
    exp = datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)
    defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
    if defro == 1:
        pro_name = "초코 빅카롱(쇼케이스)"
        method = "냉장"
        today = datetime.datetime.now()
        defro_start = today.strftime('%Y-%m-%d %H:%M')
        defro_end = (today + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M')
    if defro == 2:
        pro_name = "초코 빅카롱"
        method = "냉동"

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
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(hours=72)).strftime('%Y-%m-%d %H:%M')
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
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
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
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
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
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
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
    exp = datetime.date(y, m, d) + relativedelta(months=8) - datetime.timedelta(days=1)
    open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
    if open == 1:
        pro_name = "스프레이형 휘핑기(개봉)"
        today = datetime.datetime.now()
        open_date = today.strftime('%Y-%m-%d %H:%M')
        hold_time = (today + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
    if open == 2:
        pro_name = "스프레이형 휘핑기"

# wb_open = openpyxl.load_workbook('재고 관리표.xlsx')
# wb_append = wb_open.active
# wb_append.append([pro_name, method, exp, open_date, defro_start, defro_end, hold_time])
# wb_open.save('재고 관리표.xlsx')
# wb_open.close()

print(pro_name, method, exp, open_date, defro_start, defro_end, hold_time)