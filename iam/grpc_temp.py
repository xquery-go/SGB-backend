# add the following import statement to use server reflection
from concurrent import futures
from grpc_protos import User_pb2_grpc
from grpc_protos import User_pb2
import grpc
from grpc_reflection.v1alpha import reflection


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    User_pb2_grpc.add_UserServicer_to_server(User_pb2_grpc.User(), server)
    # the reflection service will be aware of "Greeter" and "ServerReflection" services.
    SERVICE_NAMES = (
        User_pb2.DESCRIPTOR.services_by_name['User'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()


