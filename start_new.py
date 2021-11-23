import main_func_new

print("----------재고 정리 작업을 시작합니다----------")
code = int(input("제품 코드 입력(1 ~ ?): "))

BOT = main_func_new.Cleaning()

def program(BOT, code):
    BOT.main(code)
    BOT.add_notion()
    BOT.final_result()

program(BOT, code)

while True:
    restart = int(input("다른 재고를 추가하시겠습니까?(예는 1, 아니오는 2)?: "))
    if restart == 1:
        code = int(input("제품 코드 입력(1 ~ ?): "))
        program(BOT, code)
    elif restart == 2:
        print("----------고생하셨습니다!----------")
        quit()

