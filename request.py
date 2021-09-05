# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:51:35 2021

@author: PAPU
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())