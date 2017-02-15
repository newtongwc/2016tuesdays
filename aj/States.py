states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
        'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana',
        'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada',
        'New York', 'Ohio', 'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming'
]

def Askforstart():
    a = raw_input("Put in a letter")
    for x in states:
        b = x[0].lower()
        if b == a:
            print x

def Askfor():
    a = raw_input("Put in a letter")
    for x in states:
        c =""
        for y in x:
            if y == x[0]:
                b = x[0].lower()
            if y == a:
                if c!=x:
                    getnum(x,a)
                    print x
                    c = x
            elif b == a:
                getnum(x,a)
                print x
                b = ""


def getnum(list,var):
    a = 0
    for x in list:
        if x == var:
            a = a+1
        elif x.lower() == var:
            a = a+1
    print a

Askforstart()
Askfor()
