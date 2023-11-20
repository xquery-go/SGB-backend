from core.messagbus.server import BaseAbstractService
from generated_grpc import User_pb2_grpc
from generated_grpc import User_pb2
from google.protobuf.json_format import MessageToDict, ParseDict

# from users.models import User


class UserService(BaseAbstractService):
    grpc_module = User_pb2_grpc

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
        return 'UserService'

