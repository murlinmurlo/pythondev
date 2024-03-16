#!/usr/bin/env python3
import asyncio
import cowsay
import shlex

clients = {}

async def chat(reader, writer):
    me = None
    r = asyncio.Queue()
    flag = False

    while me not in cowsay.list_cows():
        inpt = (await reader.readline()).decode().strip()
        if inpt == 'who':
            writer.write((cowsay.cowsay(' '.join([i for i in clients])) + '\n').encode())
            await writer.drain()
        elif inpt == 'cows':
            writer.write((cowsay.cowsay(' '.join(set(cowsay.list_cows()) - set([i for i in clients]))) + '\n').encode())
            await writer.drain()
        elif inpt == 'quit':
            flag = True
            break
        elif len(inpt.split()) != 2:
            continue
        else:
            login, me = inpt.split()
            if login != 'login':
                me = None
    clients[me] = r
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    while not reader.at_eof() and not f:
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())

    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
