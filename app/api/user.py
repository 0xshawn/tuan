# coding: utf-8

import datetime

from app.api import api
from common import render
# from config import environment


@api.route('/user', methods=['GET'])
def user_home():
    now = datetime.datetime.now()

    return render.ok('This is home page' + now)
