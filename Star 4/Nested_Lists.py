if __name__ == '__main__':
    Students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Students.append([name,score])

    scores = set([score[1] for score in Students])
    scores = sorted(scores)
    Second_Lowest_Scored = scores[1]
    
    names = [score[0] for score in Students if score[1] == Second_Lowest_Scored ]    
    
    names.sort()

    for name in names:
        print(name)    
