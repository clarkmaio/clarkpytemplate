'''
Functions used specifically in tesdt pipeline
'''

from prefect import task

@task(name='f1')
def test_function_1(x, y):
    return x+y

@task(name='f2')
def test_function_2(x):
    return x**2

@task(name='f3')
def test_function_3(x):
    print('RESULT', x)