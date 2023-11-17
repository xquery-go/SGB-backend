import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool

channel = grpc.secure_channel(server_address, creds)
reflection_db = ProtoReflectionDescriptorDatabase(channel)


desc_pool = DescriptorPool(reflection_db)


service_desc = desc_pool.FindServiceByName("helloworld.Greeter")
method_desc = service_desc.FindMethodByName("helloworld.Greeter.SayHello")

request_desc = desc_pool.FindMessageTypeByName("helloworld.HelloRequest")
request = MessageFactory(desc_pool).GetPrototype(request_desc)()

services = reflection_db.get_services()