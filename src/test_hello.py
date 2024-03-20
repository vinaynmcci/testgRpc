import grpc
import hello_pb2
import hello_pb2_grpc
import hello_server

def test_say_hi():
    server = grpc.server()
    hello_pb2_grpc.add_HelloServiceServicer_to_server(hello_server.HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        response = stub.SayHi(hello_pb2.HelloRequest(name='TestUser'))
        assert response.message == "Hi, TestUser"

    server.stop(0)

def test_say_hello():
    server = grpc.server()
    hello_pb2_grpc.add_HelloServiceServicer_to_server(hello_server.HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='TestUser'))
        assert response.message == "Hello, TestUser"

    server.stop(0)
