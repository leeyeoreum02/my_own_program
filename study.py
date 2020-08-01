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

def get_words(word_list):
    question_list = []
    answer_list = []
    
    random.shuffle(word_list)
    
    for index in range(len(word_list)):
        temp = word_list[index].split('=')
        question_list.append(temp[0])
        answer_list.append(temp[1])

    for index in range(len(question_list)):
        indexed_question = str(index + 1) + '.' + question_list[index]
        print(indexed_question + '\n')
        
    return answer_list