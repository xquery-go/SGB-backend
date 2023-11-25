import ipdb
import grpc
from google.protobuf.json_format import MessageToDict, MessageToJson
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import MessageFactory
from grpc_reflection.v1alpha import reflection_pb2, reflection_pb2_grpc

from generated_grpc import User_pb2
from generated_grpc import User_pb2_grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
from grpc_reflection.v1alpha.reflection_pb2 import ServerReflectionRequest
from icecream.icecream import ic

class RegistryClient:
    def __init__(self, channel_endpoint):
        self.channel_endpoint = channel_endpoint
        self._channel = grpc.insecure_channel(channel_endpoint)
        self.stub = User_pb2_grpc.UserStub(self._channel)

    def list_requests(self):
        req = User_pb2.ListRequest()
        responses = self.stub.list(req)
        for resp in responses:
            yield MessageToDict(resp, preserving_proto_field_name=True)

    def ret(self):
        req = User_pb2.UserRetrieveRequest(UserId=1)
        response = self.stub.retrieve(req)
        return MessageToDict(response, preserving_proto_field_name=True)


def run(request_message='UserRetrieveRequest'):
    print("Will try to greet world ...")
    from grpc_reflection.v1alpha.reflection_pb2_grpc import ServerReflectionStub
    with grpc.insecure_channel("iam-service:50051") as channel:
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        descriptor_pool = DescriptorPool(reflection_db)
        request_desc = descriptor_pool.FindMessageTypeByName(request_message)
        # servicer = desc_pool.FindFileContainingSymbol('User')
        service_descriptor = descriptor_pool.FindServiceByName('User')
        method_descriptor = descriptor_pool.FindMethodByName('User.retrieve')
        # request_class = request_desc.GetPrototype(input_type)
        request_class = MessageFactory(descriptor_pool).GetPrototype(request_desc)
        response_desc = descriptor_pool.FindMessageTypeByName('UserData')
        response_class = MessageFactory(descriptor_pool).GetPrototype(response_desc)

        print('On it')
        response = channel.unary_unary(
            '/{}/{}'.format(service_descriptor.full_name, method_descriptor.name),
            request_serializer=request_class.SerializeToString,
            response_deserializer=response_class.FromString,
        )(request_class(UserId=1), timeout=10)
        print("Response:", response)
        return response

import grpc
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
from grpc_reflection.v1alpha import reflection_pb2_grpc
from grpc_reflection.v1alpha import reflection_pb2
from grpc_reflection.v1alpha import reflection


def run2():
    with grpc.insecure_channel('iam-service:50051') as channel:
        # Create a reflection stub
        stub = reflection_pb2_grpc.ServerReflectionStub(channel)

        # Get the file descriptor for the service
        file_descriptor_response = stub.ServerReflectionInfo(
            iter([reflection_pb2.ServerReflectionRequest(
                file_containing_symbol='User',
            )])
        )

        # Get the file descriptor proto
        ipdb.set_trace()
        file_descriptor_proto = file_descriptor_response.next().SerializeToString()

        # Create a descriptor pool and add the file descriptor proto
        abcd = 1
        if abcd == 1:
            reflection_db = ProtoReflectionDescriptorDatabase(channel)
            descriptor_pool = DescriptorPool(reflection_db)
        else:
            descriptor_pool = _symbol_database.Default()

        defg = 1
        if defg == 2:
            file_descriptor = descriptor_pb2.FileDescriptorProto.FromString(file_descriptor_proto.decode('cp1252')[0])
            descriptor_pool.Add(file_descriptor)
        else:
            file_descriptor = file_descriptor_proto


        # Get the service descriptor
        message_type = descriptor_pool.FindMessageTypeByName('User.retrieve')
        service_descriptor = descriptor_pool.FindServiceByName('User')

        # Get the method descriptor
        method_descriptor = service_descriptor.FindMethodByName('retrieve')

        # Create a request message
        request_class = descriptor_pool.GetPrototype(method_descriptor.input_type)
        request_message = request_class(UserId=1)

        # Call the method
        response = channel.unary_unary(
            '/{}/{}'.format(service_descriptor.full_name, method_descriptor.name),
            request_serializer=request_class.SerializeToString,
            response_deserializer=descriptor_pool.GetPrototype(method_descriptor.output_type).FromString,
        )(request_message)

        print("Response:", response)
