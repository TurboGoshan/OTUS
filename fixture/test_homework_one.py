#Check the fixture with module scope
def test_one(fixture_module):
    x=[1, 2, 3, 4, 5, 6, 7, 8]
    if len(x)== 8:
        print('module test passed')

#Check the fixture with session scope
def test_two(fixture_session):
    x=(1, 2, 3, 4, 5, 6, 7, 8)
    if len(x)== 8:
        print('session test passed')

#Check the fixture with function scope
def test_three(fixture_function):
    x={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    if len(x)== 8:
        print('function test passed')

#Check the fixture without scope
def test_four(fixture_without):
    x={1, 2, 3, 4, 5, 6, 7, 8}
    if len(x)== 8:
        print('test without passed')

def test_five():
    x=[1, 2]
    y=[3, 4]
    z = x + y
    assert z==[1, 2, 3, 4]
