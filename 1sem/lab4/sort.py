import random

def quick(m):
   if len(m) > 1:
       a = random.choice(m)
       less = []
       more = []
       equal = []
       for x in m:
           if x < a:
               less += [x]
           elif x > a:
               more += [x]
           else:
               equal += [x]
       return quick(less) + equal + quick(more)
   else:
       return m
def rascheska(m):
    l = len(m)
    factor = 1.247
    gap = l/factor
    while gap > 1:
        i = 0
        j = round(gap)
        while j < l:
            if m[i] > m[j]:
                m[i],m[j]=m[j],m[i]
            i += 1
            j += 1
        gap = gap/factor
    return m