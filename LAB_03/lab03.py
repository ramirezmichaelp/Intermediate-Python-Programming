#michael p ramirez

def power(n, k):
    if( k == 0):
        return 1
    else:
        return n * power(n, k - 1)
    
    


#############################################
def integerDivision(n,k):
    score=0 #create tracker
    
    if (n<k): #base case
        return score
    else:
        score +=1#increase by one because our base case not meet
        return integerDivision(n-k,k)+score


##########################################
def collectVowels(s):
    v="aeiouAEIOU" #these are my targets
    
    #base case of empty string
    if len(s)==0:
        return []
    
    
    else:

        if s[0] in v:
            return  list(s[0]) + collectVowels(s[1:])
        
    
        else:
            return  collectVowels(s[1:])
        
#################################################################################
def reverseString(s):
    
    if len(s)==0: #base case of empty string
        return s
    else:
        return reverseString(s[1:])+s[0]
    

############################
def removeSubString(s, sub):
    #let create some variable to use
    x=len(s)
    y=len(sub)
    
    if y>x or y==0: #base case sub is empty or len of string is less than
                    #sub  
        return s
    
    else:
        
        if s[:y]==sub:
            
            return removeSubString(s[y:], sub)
        
        else:
            
            return s[0]+removeSubString(s[1:], sub)
      
