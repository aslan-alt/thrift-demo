import sys

sys.path.append('gen-py')
from thrift.transport import TSocket, TTransport
from thrift.protocol import TCompactProtocol
from calculate import Calculate
from base.ttypes import InvalidaOperation,Work,Operation

def main():
    # 创建传输工具对象
    transport = TTransport.TBufferedTransport(TSocket.TSocket('127.0.0.1', 8880))
    # 创建消息协议工具对象
    protocol = TCompactProtocol.TCompactProtocol(transport)

    # 创建用于进行RPC调用的客户端对象
    client = Calculate.Client(protocol)
    # 打开连接
    transport.open()
    # 进行具体的过程调用
    client.ping()
    print('调用了pin-----')
    result = client.divide(100, 50)
    print('100/50={}'.format(result))

    try:
        result = client.divide(100, 0)
    except InvalidaOperation as e:
        print(e.why)

    work = Work()
    work.op = Operation.ADD
    work.num2 = 200
    work.num1 = 100
    # 可以简写为 Work(100,200,Operation.ADD)
    result2 = client.calculate(work)
    print('result2----------')
    print(result2)
    # 关闭连接
    transport.close()


if __name__ == '__main__':
    main()
