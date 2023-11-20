import ipdb
import grpc
from google.protobuf.json_format import MessageToDict

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


if __name__ == '__main__':
    reg = RegistryClient('[::]:50051')
    abcd = reg.ret()
    print(abcd.__dict__)

