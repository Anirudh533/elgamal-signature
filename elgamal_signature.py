import math
def signver(p,al,be,x,gam,delta):
    if pow(al,x)%p == (pow(be,gam) * pow(gam,delta))%p:
        return "Signature matched!"
    else:
        return "Signature did not match!"

print(signver(31847,5,26379,20543,20679,11082))

def dislog(be,al,p):
    # be = 26379
    # al = 5
    # p = 31847
    for a in range(1,p):
        temp = (al**a)%p
        if be == temp:
            return a
print(dislog(26379,5,31847))

def nondislog(delta,x,a,gam,p):
    t = (x-(a*gam))%(p-1)
    q = math.gcd(delta,p-1)
    f = pow((int)(delta/q), -1, (int)((p-1)/q))
    final = ((t/q * f)%((p-1)/q))
    for i in range(1,q):
        k = final + (i * ((p-1)/q))
    return int(k)
print(nondislog(11082,20543,7973,20679,31847))

