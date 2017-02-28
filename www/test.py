import orm
from models import User, Blog, Comment
import asyncio

async def destory_pool():

    #global __pool
    if orm.__pool is not None :
        orm.__pool.close()
        await orm.__pool.wait_closed()

async def test():
    await orm.create_pool(loop,user='root', password='mysql', db='awesome')

    u = User(name='Test', email='test6@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    # await User(id='0014881168199670ae1cd311c2c4aad9b31dbb9bcb312ae000').remove()
    # r = await User.findAll()
    # print(r)
    # await destory_pool()

loop = asyncio.get_event_loop()

loop.run_until_complete(test())

loop.close()
