def solution(h1, m1, s1, h2, m2, s2):

    def get(ss):
        
        hcount = int(ss / (43200/719))
        mcount = int(ss / (3600/59))
        panelty =  2 if 43200 <= ss else 1
        
        return hcount + mcount - panelty     

    ss1 = h1*3600 + m1*60 + s1
    ss2 = h2*3600 + m2*60 + s2
    
    s = get(ss1)
    e = get(ss2)
    snow = ss1 * 719 % 43200 == 0 or ss1 * 59 % 3600 == 0

    
    return e - s + snow