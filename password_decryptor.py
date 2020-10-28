#%%
def replace_zeros(s, pos):
    new_s = list(s)
    j=0
    for p in reversed(pos):
        new_s[p]=s[j]
        j+=1
    del new_s[0:j]
    return new_s

def zero_pos(s):
    result = []
    for x in range(len(s)):
        if is_zero(s[x]): result.append(x)
    return result

def is_zero(n):
       try:
           int(n)
       except ValueError:
           return False
       return int(n)==0

def flipchar(s, pos):
    new_s = s
    for p in pos:
        j=p-2
        new_s[j:j+2] = list(reversed(s[j:j+2]))
    return new_s

def ast_pos(s):
    result = []
    for x in range(len(s)):
        if s[x]=='*': result.append(x)
    return result

def remove_ast(s):
    return ''.join([c for c in s if c != '*'])

#--------main
s = '51Pa*0Lp*0e'

nozero_s = replace_zeros(s, zero_pos(s))
password = flipchar(nozero_s, ast_pos(nozero_s))
password = remove_ast(password)

print(password)