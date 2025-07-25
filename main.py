classes = []
while True:
    try:
        s = input()
        if "class" in s:
            classes.append(s)
    except:
        break

def fix_name(s):
    s = s.replace(',', '')
    s = s.replace(':', '')
    return s

extends_class = {}
for _class in classes:
    parts = _class.split()
    classname = fix_name(parts[1])
    extend_class = []
    if len(parts) >= 3:
        for i in range(3, len(parts)):
            extend_class.append(fix_name(parts[i]))

    extends_class[classname] = extend_class

for i in range(len(extends_class)):
    for classname in extends_class:
        for nextclass in extends_class[classname]:
            for newclass in extends_class[nextclass]:
                if newclass not in extends_class[classname]:
                    extends_class[classname].append(newclass)

flag = True
for classname in extends_class:
    if classname in extends_class[classname]:
        flag = False

if flag:
    print('possible')
else:
    print('impossible')
