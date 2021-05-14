def get_max_feq(str):
    max_occur=0
    max_element=str[0]
    for element in str:
        current_count=str.count(element)
        if current_count>max_occur:
            max_occur=current_count
            max_element=element

    return max_element

if __name__ == '__main__':
    res=get_max_feq(['a','b','c','a'])
    print(res)
