import grpc
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.json_format import MessageToDict
from google.protobuf.message_factory import MessageFactory
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)

from generated_grpc import User_pb2
from generated_grpc import User_pb2_grpc


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
