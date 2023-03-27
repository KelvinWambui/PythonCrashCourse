
import datetime
from datetime import date

import time

todaytime=time.timezone

today=date.today()

import validate 
from validate import validateemail
email='test@test.com'

if validateemail(email) :
    print('Email is Valid')
else :
    print('email is not valid')

