#!/usr/bin/env python
from Cup import *

cup1 = Cup()

cup1.topupfull()
cup1.check()

cup1.empty()
cup1.check()

cup1.topuphalf()
cup1.topup(5)
cup1.observe()
cup1.check()

cup1.topupfull()
cup1.topup(1)
cup1.check()
