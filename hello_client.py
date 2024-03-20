import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.HelloServiceStub(channel)
    response = stub.SayHi(hello_pb2.HelloRequest(name='Alice'))
    print("Response from server:", response.message)
    response = stub.SayHello(hello_pb2.HelloRequest(name='Bob'))
    print("Response from server:", response.message)

if __name__ == '__main__':
    run()
