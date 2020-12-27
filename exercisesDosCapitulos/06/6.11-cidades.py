cities = {
    'kosnia': {
        'localização': 'Brasil',
        'população': '852.655',
        'fundação': '182 ac',
        'prefeito': 'Robison',
        'IDH': '0,563',
    },
    'kamia': {
        'localização': 'brasil',
        'população': '123.200',
        'fundação': '125',
        'prefeito': 'Camilo',
        'IDH': '0,863',
    },
    'Manmia' : {
        'localização': 'brasil',
        'população': '451.232',
        'fundação': '1852',
        'prefeito': 'Adomo',
        'IDH': '0,763',
    },
    'citomia' : {
        'localização': 'dionia',
        'população': '852.696',
        'fundação': '9.521 AC',
        'prefeito': 'Victus',
        'IDH': '0,853',
    }
}
for cidade in cities.keys():
    print(f'\n{cidade.upper()}')
    for info, item in cities[cidade].items():
        print(f'{info.title()}: {item.title()}')
        