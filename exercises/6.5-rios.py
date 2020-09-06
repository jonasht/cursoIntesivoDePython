rios = {
    'amazonas': 'brazil',
    'mogi guaçu': 'brasil',
    'nilo': 'egito'
}
def l(): print(30*'¨')
l()
for p, r in rios.items():
    print(p.title(), r.title())
    print(f'o rio {p.title()} corre no {r.title()}.\n')
l()    
