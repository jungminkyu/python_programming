'''
yesterday.txt 파일을 읽어서
yesterday 단어를 세는 프로그램

open mode
r : read(default), w: write
rb : read binary, wb : write binary
a : append
'''

def file_read(file_name):
    with open(file_name, "r", encoding = 'utf-8') as file:
        lyric = file.read()
        #print(lyric)
        return lyric

read = file_read("yesterday.txt")
#ctrl + alt + v : 왼쪽에 변수 생성
print(read)
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')
n_of_YESTERDAY = read.count("Yesterday")
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')
n_of_YESTERDAY = read.lower().count("yesterday")
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')

