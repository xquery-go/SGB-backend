import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool


def start_microservice(port):
    server_address_microservice = port
    channel_microservice = grpc.insecure_channel(server_address_microservice)
    reflection_db_microservice = ProtoReflectionDescriptorDatabase(channel_microservice)
    desc_pool_1 = DescriptorPool(reflection_db_microservice)
    return desc_pool_1
