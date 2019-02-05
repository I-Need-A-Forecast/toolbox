from pylogic.prejsondeepcopy import prejson

x = {
    'foo': 'barr',
    'grapht': [
        {'loc': 'mock'},
        {'park': ''},
        ['gret', 'trap', 'snarp']
    ],
    'haft': {
        'trheth': {
            'par': 'par',
            'mor': ''
        },
        'fil': []
    }
}


testx = prejson(x)
print(testx)