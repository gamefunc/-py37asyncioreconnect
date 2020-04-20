import asyncio


class connect1(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print("connect ok")


    def data_received(self, data):
        print(data)
        self.transport.write(data)

    async def reconnect(self):
        while 1:
            try:
                print("try reconnect")
                loop = asyncio.get_event_loop()
                dst_transport, dst_protocol =  await loop.create_connection(
                            connect1, "127.0.0.1", 7777)
                break
            except:
                await asyncio.sleep(3)
                
    def connection_lost(self, *args):
        print("break")
        task = asyncio.create_task(self.reconnect())




loop = asyncio.get_event_loop()
coro = loop.create_connection(
    conect1, "127.0.0.1", 7777)
server = loop.run_until_complete(coro)
loop.run_forever()
