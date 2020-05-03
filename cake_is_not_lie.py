def solution(s):
    length = len(s)  
    for x in range(1,length):
        if (length % x == 0):
            lis =[s[y:y+x] for y in range(0,length,x) ] 
            lis_len = len(lis)
            for z in range(0,lis_len-1):
                if (lis[z] == lis[z+1]): 
                    if (z==lis_len-2):
                        return lis_len
    return lis_len


# print(solution("abcabcabcabc"))
