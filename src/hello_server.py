import grpc
import hello_pb2
import hello_pb2_grpc
from concurrent import futures

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHi(self, request, context):
        return hello_pb2.HelloResponse(message="Hi, " + request.name)

    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message="Hello, " + request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
