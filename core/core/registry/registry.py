import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase

# Microservice 1 - Port 8000
server_address_microservice1 = 'localhost:8000'
channel_microservice1 = grpc.insecure_channel(server_address_microservice1)
reflection_db_microservice1 = ProtoReflectionDescriptorDatabase(channel_microservice1)

# Microservice 2 - Port 8001
server_address_microservice2 = 'localhost:8001'
channel_microservice2 = grpc.insecure_channel(server_address_microservice2)
reflection_db_microservice2 = ProtoReflectionDescriptorDatabase(channel_microservice2)