def es_ama(string_1: str , string_2: str) -> bool:
    string_1 = string_1.lower()
    string_2 = string_2.lower()

    if string_1 == string_2:
        return False
    
    return sorted(string_1) == sorted(string_2)


print(es_ama("amor" , "roma"))





    





