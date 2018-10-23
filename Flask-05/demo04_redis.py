from redis import  StrictRedis

def redis_set_kv():
    """使用redis设置键值对数据"""
    # 使用默认值的方式创建redis对象
    #decode_responses=True 将二进制的数据decode成字符串
    sr = StrictRedis(decode_responses=True)
    #设置键值对
    sr.set("name111","yaoming")
    print(sr.get("name111"))

if __name__ == '__main__':
    redis_set_kv()

