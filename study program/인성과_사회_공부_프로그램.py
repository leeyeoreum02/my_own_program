from study import get_words

mode = int(input("단원을 선택하시려면 '0', 오답학습을 하시려면 '1'을 입력하세요: "))

if mode == 0:
    chapter_num = int(input("몇 단원의 단어를 학습하시겠습니까? "))

    with open('인성과_사회_{}장.txt'.format(chapter_num), 'r', encoding='UTF-8') as file:
        word_list = file.read().split('>')
        answer = get_words(word_list)
        
        get_answer = input("답을 출력하시겠습니까?('y' or 'n') ")
                
        if get_answer == 'y':
            for index in range(len(answer)):
                print("{}. {}".format((index + 1), answer[index]))
        elif get_answer == 'n':
             print("답을 출력하지 않았습니다.\n")

elif mode == 1:
    wrong_num = int(input("몇 단원의 오답노트를 학습하시겠습니까? "))
    
    with open('인성과_사회_{}장_오답노트.txt'.format(wrong_num), 'r', encoding='UTF-8') as file:
        word_list = file.read().split('>')
        answer = get_words(word_list)
        
        get_answer = input("답을 출력하시겠습니까?('y' or 'n') ")
                
        if get_answer == 'y':
            for index in range(len(answer)):
                print("{}. {}".format((index + 1), answer[index]))
        elif get_answer == 'n':
             print("답을 출력하지 않았습니다.\n")