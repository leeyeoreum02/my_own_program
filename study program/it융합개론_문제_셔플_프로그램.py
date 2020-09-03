import random

def get_QNA(QNA_list):
    question_list = []
    answer_list = []
    
    random.shuffle(QNA_list)
    
    for index in range(len(QNA_list)):
        temp = QNA_list[index].split('#')
        question_list.append(temp[0])
        answer_list.append(temp[1])

    for index in range(len(question_list)):
        indexed_question = str(index + 1) + '.' + question_list[index]
        print(indexed_question + '\n')
        
    return answer_list

print("""it융합개론 기말고사 학습 프로그램입니다.
학습하실 챕터를 숫자로 입력해주세요.
종료하시려면 '0'을 입력해주세요.""")
     
while True:
    chapter = int(input("어떤 챕터의 문제를 학습하시겠습니까? "))

    if chapter in range(1, 11):
        with open('CH{}_question.txt'.format(chapter), 'r', encoding='UTF-8') as file:
            QNA_list = file.read().split('.')
            answer = get_QNA(QNA_list)
            
            get_answer = input("답을 출력하시겠습니까?('y' or 'n') ")
            
            if get_answer == 'y':
                for index in range(len(answer)):
                     print("{}. {}".format((index + 1), answer[index]))
            elif get_answer == 'n':
                print("답을 출력하지 않았습니다.\n")
                
    elif chapter == 0:
        print("학습을 종료합니다.")
        break
    
    elif chapter == 11:
        with open('오답노트.txt', 'r', encoding='UTF-8') as file:
            QNA_list = file.read().split('.')
            answer = get_QNA(QNA_list)
            
            get_answer = input("답을 출력하시겠습니까?('y' or 'n') ")
            
            if get_answer == 'y':
                for index in range(len(answer)):
                     print("{}. {}".format((index + 1), answer[index]))
            elif get_answer == 'n':
                print("답을 출력하지 않았습니다.\n")