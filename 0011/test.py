def goodVsEvil(good,evil):
    goodValues=[1,2,3,3,4,10]
    evilValues=[1,2,2,2,3,5,10]
    goodsum,evilsum=0,0
    for i,g in enumerate(good.split()):
        goodsum = goodsum +goodValues[i]*int(g)
    for i,e in enumerate(evil.split()):
        evilsum = evilsum + evilValues[i]*int(e)

    if goodsum >evilsum:
        print('Good win.')
    elif goodsum == evilsum:
        print('equal.')
    else:
        print('evil win.')

if __name__=='__main__':
    good=input('Good:')
    evil=input('Evil:')
    goodVsEvil(good,evil)
