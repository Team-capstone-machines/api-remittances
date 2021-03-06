#!/usr/bin/python3
""" Helper functions.
"""


def Encrypt(number):
    """ This function encrypt the cell number.
    Return: The encrypted number.
    """
    import hashlib

    pwd = number
    key = pwd.encode('utf-8')
    return hashlib.md5(key).hexdigest()


def Convert_int(number):
    """ This function takes a string with number
    and the convert in integer.
    Return: The number converted.
    """
    # The conditions to convert the string in integer
    if number.find('.') != -1:
        list_cash = number.split('.')
        return int(list_cash[0].replace(",", "").replace("$", ""))
    if number.find('+') != -1:
        return int(number.replace('+ ', ''))
    else:
        return int(number.replace('- ', ''))


def Verify_number(cellphone, token):
    """ This function consumes the API to verify if the cell
    number is registered in the database of Mexico.
    Return: the name of the person that is register this number.
    """
    import requests

    # The API URL
    url = "https://nufi.azure-api.net/enriquecimientoinformacion/v1/busqueda"
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": token
    }
    # The body of the API to do the query
    body = "{\n  \"telefono\": \"" + cellphone + "\"\n}"
    # The requests to the API
    response = requests.post(url, data=body, headers=headers)
    # The conditions to check the information
    if response.status_code == 200:
        if response.json()['data']['person'] is not None:
            return response.json()['data']['person']['names'][0]['display']
        else:
            return 'Phone not registered to any person'
    if response.status_code == 400:
        return response.json()['message']


def Delete_GMT(hist_dict):
    for date in hist_dict:
        del_gmt = date['date'].replace('GMT', '')
        date['date'] = del_gmt
    return hist_dict
