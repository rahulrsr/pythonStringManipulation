from collections import Counter

def get_max_occur(a):
    a_ctr=Counter(a)
    print(a_ctr.most_common(1))
    print(a_ctr)


if __name__ == '__main__':
    a=input()
    a=list(a)
    get_max_occur(a)
