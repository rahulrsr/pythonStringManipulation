def rev_sec_word(statement):
    stm=statement.split()
    l=len(stm)
    new_stm=[]
    if l==1:
        return statement
    else:
        for i in range(0,l,1):
            if i%2==0:
                new_stm.append(stm[i])
            else:
                new_stm.append(stm[i][::-1])
    new_stm=' '.join(new_stm)
    return new_stm

if __name__ == '__main__':
    m=input("Enter the stament for processing")
    print(rev_sec_word(m))
