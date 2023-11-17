from core.messagbus.server import BaseAbstractService
from generated_grpc import User_pb2_grpc
# from users.models import User


class UserService(BaseAbstractService):
    grpc_module = User_pb2_grpc

    @property
    def get_add_servicer_method(self):
        return self.grpc_module.add_UserServicer_to_server

    class UserServicer(User_pb2_grpc.UserServicer):

        def get_queryset(self):
            from users.models import User
            return User.objects.all()

        def list(self, request, context):
            yield self.get_queryset()

        def retrieve(self, request, context):
            print(f'Retrieve Context {context}\n\n')
            print(f'Retrieve request {request}')
            queryset = self.get_queryset().filter(UserId=1).get()
            return str(queryset)

        def authenticate_token(self, request, context):
            print(f'Retrieve Context {context}\n\n')
            print(f'Retrieve request {request}')
            queryset = self.get_queryset().filter(UserId=1)
            return str(queryset)

    __servicer = UserServicer()

    @property
    def servicer(self):
        return self.__servicer

    @property
    def label(self):
        return 'UserService'

