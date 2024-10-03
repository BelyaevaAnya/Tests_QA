import calc_script


def test_add():
    if calc_script.add(1, 2) == 3:
        print('Test add(a,b) is OK')
    else:
        print('Test add(a,b) is fail')


def test_sub():
    if calc_script.sub(2, 2) == 0:
        print('Test sub(a,b) is OK')
    else:
        print('Test sub(a,b) is fail')


def test_mul():
    if calc_script.mul(3, 2) == 6:
        print('Test mul(a,b) is OK')
    else:
        print('Test mul(a,b) is fail')


def test_div():
    if calc_script.div(6, 2) == 3:
        print('Test div(a,b) is OK')
    else:
        print('Test div(a,b) is fail')


def test_all():
    test_add()
    test_sub()
    test_mul()
    test_div()


test_all()
