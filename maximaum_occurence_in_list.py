from collections import Counter

def most_frequent(List):
    occurence_count=Counter(List)
    print(occurence_count)
    return occurence_count.most_common(1)[0][0]


if __name__ == '__main__':
    #List=list(input())
    List = [2, 1, 2, 2, 1, 3]
    print(most_frequent(List))