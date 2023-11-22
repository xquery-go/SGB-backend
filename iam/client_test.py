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


def run(request_message: str):
    print("Will try to greet world ...")
    from grpc_reflection.v1alpha.reflection_pb2_grpc import ServerReflectionStub
    with grpc.insecure_channel("iam-service:50051") as channel:
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        desc_pool = DescriptorPool(reflection_db)
        desc_pool.FindMessageTypeByName(request_message)
        servicer = desc_pool.FindFileContainingSymbol('User')
        user_servicer = servicer.services_by_name['User']
        method = user_servicer.methods_by_name['retrieve']

        ipdb.set_trace()
        requests = [MessageFactory(desc_pool).GetPrototype(request_desc)(UserId=1)]

        reflection_stub = ServerReflectionStub(channel)
        reflection_request = ServerReflectionRequest()
        response = reflection_stub.ServerReflectionInfo((req for req in requests))
        response.next()
        print('On it')



################################################################
def make_dynamic_grpc_call(server_address, service_name, method_name, request_data):
    with grpc.insecure_channel(server_address) as channel:
        # Create a reflection stub
        stub = reflection_pb2_grpc.ServerReflectionStub(channel)

        # Use reflection to find the service descriptor
        service_descriptor_response = stub.ServerReflectionInfo(
            iter([ServerReflectionRequest(
                list_services=service_name
            )])
        )

        # Extract the service descriptor
        ipdb.set_trace()
        service_descriptor = None
        for r in service_descriptor_response:
            if r.HasField('list_services_response'):
                for service in r.list_services_response.service:
                    if service.name == service_name:
                        service_descriptor = service
                        break

        if not service_descriptor:
            print(f"Service '{service_name}' not found.")
            return

        file_containing_symbol = f"{service_name}/{method_name}"
        ic(file_containing_symbol)
        # Use reflection to find the method descriptor
        method_descriptor_response = stub.ServerReflectionInfo(
            iter([ServerReflectionRequest(
                file_containing_symbol=file_containing_symbol
            )])
        )
        ipdb.set_trace()
        # Extract the method descriptor
        method_descriptor = None
        for r in method_descriptor_response:
            if r.HasField('file_descriptor_response'):
                method_descriptor = r.file_descriptor_response.service[0].method[0]
                break

        if not method_descriptor:
            print(f"Method '{method_name}' not found in service '{service_name}'.")
            return

        # Create a dynamic request message
        request_class = method_descriptor.input_type
        request = request_class(**request_data)

        # Make the gRPC call dynamically
        method_full_name = f"/{service_name}/{method_name}"
        call = channel.unary_unary(method_full_name)
        response = call(request)

        print(f"Response: {MessageToJson(response)}")

# Example usage
# make_dynamic_grpc_call("your_grpc_server:50051", "YourService", "YourMethod", {"UserId": 1})
