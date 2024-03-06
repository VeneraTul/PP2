'''sentence=input()
cntL=0
cntU=0
for x in sentence:
    if x>="a" and x<="z":
        cntL+=1
    if x>="A" and x<="Z":
        cntU+=1
print(f"the number of upper case letters {cntU} and lower case letters {cntL}")'''


def upper_case_letter(sen):
    for x in sen:
     if x>="A" and x<="Z":
        return True
    return False
   

def lower_case_letter(sen):
    for x in sen:
         if x>="a" and x<="z":
             return True
    return False
        
sentence=input()

letters_isUpper = list(map(upper_case_letter, sentence))
letters_isLower = list(map(lower_case_letter, sentence))

amount_of_Upper = sum(letters_isUpper)
amount_of_Lower = sum(letters_isLower)

print(f"the number of upper case letters {amount_of_Upper} and lower case letters {amount_of_Lower}")