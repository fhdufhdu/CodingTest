def solution(h1, m1, s1, h2, m2, s2):

    def get(ss):
        """
        한 시간은 43200초이고 시침이 한번 돌 때마다 60초가 흘러가므로
        시침과 초침은 총 43200/60 = 720번 만난다.
        이때, 0시 0분 0초는 만났다고 칠 수 없으므로 720-1 = 719번 만난다
        그럼 시침과 초침은 43200/719초마다 한번씩 만난다.
		분침도 똑같이 계산하면 된다.
        """
        hcount = int(ss / (43200/719))
        mcount = int(ss / (3600/59))
        panelty =  2 if 43200 <= ss else 1
        
        return hcount + mcount - panelty     

    ss1 = h1*3600 + m1*60 + s1
    ss2 = h2*3600 + m2*60 + s2
    
    s = get(ss1)
    e = get(ss2)
    """
   	e에서 s를 뺀다는 소리는 h1시 m1분 s1초를 포함하지 않고 계산 한 것과 같다.
	---------------------------------------------------------
	  e => 0시 0분 0초 ~ h1시 m1분 s1초 ~ h2시 m2분 s2초
	- s => 0시 0분 0초 ~ h1시 m1분 s1초
	---------------------------------------------------------
	result:h1시 m1분 s1 + 1초 ~ h2시 m2분 s2초
    
    그러므로 s1이 알람을 울려야하는 시간인지에 대한 여부를 판단하는 것이 필요하다.
    0시 0분 0초 혹은 12시 0분 0초일때 알람을 울리면 된다.
    """
    s_now = h1 % 12 == 0 and m1 == 0 and s1 == 0

    
    return e - s + s_now