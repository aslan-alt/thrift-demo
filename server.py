import sys

sys.path.append('gen-py')
from calculate import Calculate
from base.ttypes import InvalidaOperation, Operation
from thrift.protocol import TCompactProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TServer


# 实现接口服务器的具体方法
class CalculateHandle(Calculate.Iface):
    def ping(self):
        with open('./test_runoob.txt', 'w+') as file:
            file.write('hello world !')



    def divide(self, num1, num2):
        if num2 == 0:
            raise InvalidaOperation(0, 'cannot divide by 0')
        return num1 / num2

    def calculate(self, w):
        if w.op == Operation.ADD:
            return w.num1 + w.num2
        elif w.op == Operation.SUBTRACT:
            return w.num1 * w.num2
        else:
            raise InvalidaOperation(w.op, 'invalid Operation')


if __name__ == '__main__':
    # 开启服务器，对外提供RPC远程调用
    # 构建rpc 处理调用工具
    handler = CalculateHandle()
    processor = Calculate.Processor(handler)

    # 构建消息协议工具
    pFactory = TCompactProtocol.TCompactProtocolFactory()
    # 构建传输工具
    transport = TSocket.TServerSocket('127.0.0.1', 8880)
    tfactory = TTransport.TBufferedTransportFactory()
    # 构建服务器对象
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pFactory)
    # 开启服务
    print('服务已开启')
    server.serve()
