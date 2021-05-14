def reverse_sentence(statement):
    stm=statement.split()
    rev_stm=stm[::-1]
    rev_stm=' '.join(rev_stm)
    return rev_stm

if __name__ == '__main__':
    m=input("Enter the sentence to be reversed: ")
    print(reverse_sentence(m))

