import asyncio
import requests


class SendMessageRequest:
    def __init__(self, id, base_url, path, params, data):
        self.data = id
        self.base_url = base_url
        self.path = path
        self.params = params
        self.data = data

class SendMesageResponse:
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

class BatchSendMessageRequest:
    def __init__(self, url, batch: list):
        self.url = url
        self.batch = batch
    

class BatchSendMesageResponse:
    def __init__(self, total, failed: list):
        self.failed = failed
        self.total = total



def batch_send_messages(req_batch: BatchSendMessageRequest, headers = {}) -> BatchSendMesageResponse:
    batchRequest = BatchSendMessageRequest
    batchResponse = BatchSendMesageResponse
    asyncio.run(make_requests(req_batch))
    return 


async def make_requests(req_batch):
    return await aaa(req_batch)

async def aaa(req_batch):
    responses = {}
    for msg_req in req_batch.batch:
        responses[msg_req.id] = await requests.post(msg_req.url, headers=msg_req.headers, data=msg_req.data)
    return responses

async def test(i):
    await asyncio.sleep(1)
    print("testea3 " + str(i))
    return 
    

async def main():
    tasks = []
    for i in range(0,5):
        tasks.append(asyncio.create_task(   test(i)))
    print("uwu")
    l = await asyncio.gather(*tasks)
    #asyncio.gather(test(1),test(2))
    print("asdasdas")
    return     

if __name__ ==  '__main__':
    asyncio.run(main())