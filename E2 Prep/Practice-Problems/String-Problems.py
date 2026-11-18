def reverse_string(s):
    start = 0
    end = len(s) - 1
    
    while end >= start:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    return ''.join(s)
        
def  is_palidrome(s):
    start = 0;
    end = len(s) - 1;
    
    while(start < end):
        if(s[start] != s[end]):
            return False   
        start += 1
        end -= 1
        
    return True

def countVowels(s):
    count = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            count += 1
    
    return count