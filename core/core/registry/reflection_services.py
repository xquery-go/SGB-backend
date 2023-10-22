from concurrent import futures
import grpc

from grpc_reflection.v1alpha import reflection
from project_a import your_proto_file_a_pb2_grpc

server = grpc.server(futures.ThreadPoolExecutor())

your_proto_file_a_pb2_grpc.add_YourServiceServicer_to_server(
    YourServiceImplementationA(), server
)

SERVICE_NAMES = (
    your_proto_file_a_pb2.DESCRIPTOR.services_by_name['YourService'].full_name,
)
reflection.enable_server_reflection(SERVICE_NAMES, server)
server.add_insecure_port('[::]:50051')  # You can specify the desired port
server.start()
