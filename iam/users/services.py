from core.messagbus.server import BaseAbstractService
from generated_grpc import User_pb2_grpc
from generated_grpc import User_pb2
from generated_grpc import HelloWorld_pb2
from generated_grpc import HelloWorld_pb2_grpc
from google.protobuf.json_format import MessageToDict, ParseDict

# from users.models import User


class UserService(BaseAbstractService):
    grpc_module = User_pb2_grpc
    pb2_module = User_pb2

    class Servicer(User_pb2_grpc.UserServicer):

        def get_queryset(self):
            from users.models import User
            return User.objects.all()

        def list(self, request, context):
            queryset = self.get_queryset()
            for user_data in queryset:
                data = {
                    "UserId": user_data.UserId,
                    "UserName": user_data.username,
                    "EmailAddress": user_data.email,
                }
                yield ParseDict(data or {}, User_pb2.UserData())

        def retrieve(self, request, context):
            print(f'Retrieve Context {context}\n\n')
            print(f'Retrieve request {request}')
            queryset = self.get_queryset().filter(UserId=1).get()
            data = {
                "UserId": queryset.UserId,
                "UserName": queryset.username,
                "EmailAddress": queryset.email,
            }
            response = ParseDict(data, User_pb2.UserData())
            print(f'response ::: \n {response}')
            return response

        def authenticate_token(self, request, context):
            print(f'Retrieve Context {context}\n\n')
            print(f'Retrieve request {request}')
            queryset = self.get_queryset().filter(UserId=1)
            return str(queryset)

    __servicer = Servicer()

    @classmethod
    def get_add_servicer_method(cls, server, servicer=None):
        return cls.grpc_module.add_UserServicer_to_server(cls.__servicer, server)

    def servicer(self) -> Servicer:
        return self.__servicer

    @property
    def label(self) -> str:
        return 'User'


class GreetingService(BaseAbstractService):
    grpc_module = HelloWorld_pb2_grpc
    pb2_module = HelloWorld_pb2

    class Servicer(grpc_module.GreeterServicer):

        def personal(self, request, context):
            reply = f'Your message was {request.message}, to that i would say Hello'
            data = {
                "ReturnGreeting": reply,
            }
            response = ParseDict(data, HelloWorld_pb2.HelloReply())
            return response

        # def parrot(self, request, context):
        #     """Missing associated documentation comment in .proto file."""
        #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        #     context.set_details('Method not implemented!')
        #     raise NotImplementedError('Method not implemented!')
        #
        # def chatty(self, request_iterator, context):
        #     """Missing associated documentation comment in .proto file."""
        #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        #     context.set_details('Method not implemented!')
        #     raise NotImplementedError('Method not implemented!')
        #
        # def bidirectional(self, request_iterator, context):
        #     """Missing associated documentation comment in .proto file."""
        #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        #     context.set_details('Method not implemented!')
        #     raise NotImplementedError('Method not implemented!')

    __servicer = Servicer()

    @classmethod
    def get_add_servicer_method(cls, server, servicer=None):
        return cls.grpc_module.add_GreeterServicer_to_server(cls.__servicer, server)

    def servicer(self) -> Servicer:
        return self.__servicer

    @property
    def label(self) -> str:
        return 'Greeter'

