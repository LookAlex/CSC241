def rps(p1, p2):
    if p1.upper()==p2.upper():
            print(0)
    if p1.upper()=='R':
        if p2.upper()=='P':
            print(1)
    if p1.upper()=='R':
        if p2.upper()=='S':
            print(-1)
    if p1.upper()=='P':
        if p2.upper()=='S':
            print(1)
    if p1.upper()=='P':
        if p2.upper()=='R':
            print(-1)
    if p1.upper()=='S':
        if p2.upper()=='P':
            print(-1)
    if p1.upper()=='S':
        if p2.upper()=='R':
            print(1)
def mystery(n):
    counter=0
    while n>1:
        n=n//2
        counter+=1
    return counter
