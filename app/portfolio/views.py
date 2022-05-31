from django.shortcuts import render
from rest_framework.decorators import api_view
from decouple import config
import requests
from django.http import JsonResponse
import pandas as pd
from collections import defaultdict
import json

# Create your views here.
@api_view(['GET'])
def get_portfolio(request,period):
  url = f'https://paper-api.alpaca.markets/v2/account/portfolio/history?period={period}'

  headers = {
    "APCA-API-KEY-ID": config("ALP_AK"),
    "APCA-API-SECRET-KEY": config("ALP_AS"),
  }

  r = requests.get(url,headers=headers)
  l1 = []
  equityArr =[]
  l2=[]
  i=0
  p=0
  for x in r.json()['timestamp']:
      l1 .append({'id':i,'timestamp':x})
      i+=1
  for y in r.json()['equity']:
      l2.append({'id':p,'equity':y})
      p+=1


  
  df1 = pd.DataFrame(l1).set_index('id')
  df2 = pd.DataFrame(l2).set_index('id')
  df = df1.merge(df2, left_index=True, right_index=True)
  df.T.to_dict()
  data = df.to_json(orient='table')
  x = json.loads(data)
  
  return JsonResponse(x, safe=False)