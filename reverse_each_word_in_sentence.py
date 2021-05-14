def rev_words_in_sentence(statement):
    stm=statement.split()
    l=[]
    for s in stm:
        l.append(s[::-1])
    final_l=' '.join(l)
    return final_l

if __name__ == '__main__':
    m=input("Enter sentence for processing: ")
    print(rev_words_in_sentence(m))