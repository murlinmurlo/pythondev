#!/usr/bin/env python3
import asyncio
import cowsay


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
    while not reader.at_eof() and not flag:
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                command = q.result().decode().split()
                if command[0] == 'who':
                    await clients[me].put(cowsay.cowsay(' '.join([i for i in clients])))
                elif command[0] == 'cows':
                    await clients[me].put(cowsay.cowsay(' '.join(set(cowsay.list_cows()) - set([i for i in clients]))))
                elif command[0] == 'say':
                    nm, *txt = command[1:]
                    await clients[nm].put(cowsay.cowsay(' '.join(txt), cow=me))
                elif command[0] == 'yield':
                    txt = command[1:]
                    for i in clients.values():
                        if i is not clients[me]:
                            await i.put(cowsay.cowsay(' '.join(txt), cow=me))
                elif command[0] == 'quit':
                    flag = True
            else:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
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
