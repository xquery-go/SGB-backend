import grpc
from grpc_reflection.v1alpha import reflection
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool


def start_microservice(port):
    server_address_microservice = port
    channel_microservice = grpc.insecure_channel(server_address_microservice)
    reflection_db_microservice = ProtoReflectionDescriptorDatabase(channel_microservice)
    desc_pool_1 = DescriptorPool(reflection_db_microservice)
    return desc_pool_1


thread_pool_size = 10


def start_reflection(service_name, service_address):
    server_microservice = grpc.server(thread_pool_size)
    reflection.enable_server_reflection(service_name, server_microservice)

    server_address_microservice = service_address
    server_microservice.add_insecure_port(server_address_microservice)
    return server_microservice.start()


def call_reflection():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        start_reflection('iam', 'localhost:8000').stop(0)
        start_reflection('sgb', 'localhost:8001').stop(0)
