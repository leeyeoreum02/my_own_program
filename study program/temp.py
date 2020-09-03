try:
    from collections import Counter
    
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be alphabet")
        
    word_count_dict = Counter(word)
    
    max_value = max(word_count_dict.values())
    max_key = max(word_count_dict.keys(), key=(lambda k: word_count_dict[k]))
    value_list = list(word_count_dict.values())
                
    if value_list.count(max_value) > 1:
        print("?")
    else:
        print(max_key)

except Exception as err:
    print(str(err))