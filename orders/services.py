import os
import requests
import json


def get_cities(City):
    payload = {
        "apiKey": os.getenv('DO_ACCESS_TOKEN'),
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {
            "FindByString": City,
            "Limit": "10"
        }
    }
    r = requests.get('https://api.novaposhta.ua/v2.0/json/', json=payload)
    region = r.json()
    region_list = list()
    if region['success']:
        # print(region)
        for i in range(len(region['data'])):
            region_list.append(region['data'][i])
    print(region_list)
    return region_list


def get_warehouses(ref):
    payload = {
        "apiKey": os.getenv('DO_ACCESS_TOKEN'),
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityRef": ref,
            "TypeOfWarehouseRef": "841339c7-591a-42e2-8233-7a0a00f0ed6f"
        }
    }
    r = requests.get('https://api.novaposhta.ua/v2.0/json/', json=payload)
    wh = r.json()
    wh_list = list()
    if wh['success']:
        # print(region)
        for i in range(len(wh['data'])):
            wh_list.append(wh['data'][i])
    # print(wh_list)
    return wh_list
