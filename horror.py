(_:=__import__,_c:="░▒▓",_l:=len,_2_:=range,__:=_("random").randint,____:=60,_11:=30,_1:=globals,l:=["█"*____ for f in _2_(_11)],d:=0,___ := (lambda w,h,o: (_1().update(d=_1()['d']+1),c:=_c[__(0,2)],_1().update(l=[[c if _11-h<=y and x>=o and x<=o+d else _1()['l'][y][x] for x in _2_(_l(_1()['l'][y]))] for y in _2_(_l(_1()['l']))]),___(_1_:=__(0,8),__(3,_11),__(0,____-_1_)) if _1()['d']<10 else "")),___(_1_:=__(0,8),__(3,_11),__(0,____-_1_)),[open(str(x).zfill(3)+"".join(l[x]), "x") for x in _2_(_l(l))])