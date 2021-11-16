#섭씨를 화씨로 변환하는 함수
def fah_convert(celsius) :
    return ((9/5) * float(celsius)) + 32

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.\n변환하고 싶은 섭씨 온도를 입력해주세요 : ")

user_input = input()
print(type(user_input), user_input)
fah = fah_convert(user_input)

print("섭씨온도 : ", float(user_input))
print(f"섭씨온도 : {user_input}")
print("화씨온도 : {0:.2f}".format(fah))
print(f"화씨온도 : {round(fah, 2)}")