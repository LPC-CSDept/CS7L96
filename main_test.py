import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    dict1 = {'name': 'KIM', 'ZIP': 94598, 'address': '1234 Grand ave'}
    main.printDict(dict1)
    dict2 = {'score': [100, 90], 'Grade': 'Senior'}
    main.printDict(dict2)
    dict3 = main.mergeDict(dict1, dict2)
    main.printDict(dict3)

    assert len(dict3) == 5
    assert dict3['Grade'] == 'Senior'
    assert dict3['name'] == 'KIM'
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
