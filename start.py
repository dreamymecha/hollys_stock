import main_def

print("----------재고 정리 작업을 시작합니다----------")
code = int(input("제품 코드 입력(1 ~ ?): "))

BOT = main_def.Cleaning()
BOT.main(code)
BOT.add_notion()

restart = int(input("다른 재고를 추가하시겠습니까?(예는 1, 아니오는 2)?: "))
if restart == 1:
    code = int(input("제품 코드 입력(1 ~ ?): "))
    BOT.main(code)
    BOT.add_notion()
elif restart == 2:
    quit()