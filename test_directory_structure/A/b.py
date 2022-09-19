'''
Author: CalmCapK
Date: 2022-09-19 08:33:30
LastEditors: CalmCapK
LastEditTime: 2022-09-19 08:57:49
'''

import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
print(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
from B.a import funa
from B.e import fune
from A.f import funf
from C.c import func
from C.g import fung
from d import fund
from h import funh



def funb():
    print('b')

if __name__=="__main__":
    funa()
    funb()
    func()
    fund()
    fune()
    funf()
    fung()
    funh()