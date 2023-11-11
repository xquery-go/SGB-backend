# add the following import statement to use server reflection
import os
from concurrent import futures

import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2_grpc
from grpc_health.v1.health_pb2 import HealthCheckResponse
from grpc_reflection.v1alpha import reflection

from generated_grpc import User_pb2
from generated_grpc import User_pb2_grpc
from users import models as user_models

# from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Configure Django settings
# settings.configure()


class UserServicer(User_pb2_grpc.UserServicer):

    def get_queryset(self):
        return user_models.User.objects.all()

    def list(self, request, context):
        yield self.get_queryset()

    def retrieve(self, request, context):
        print(f'Retrieve Context {context}\n\n')
        print(f'Retrieve request {request}')
        queryset = self.get_queryset().filter(UserId=1)
        return queryset

    def authenticate_token(self, request, context):
        print(f'Retrieve Context {context}\n\n')
        print(f'Retrieve request {request}')
        queryset = self.get_queryset().filter(UserId=1)
        return queryset


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    User_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)

    health_servicer = health.HealthServicer(experimental_non_blocking=True)
    health_servicer.set('User', HealthCheckResponse.SERVING)
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    # the reflection service will be aware of "Greeter" and "ServerReflection" services.
    print(User_pb2.DESCRIPTOR.services_by_name['User'].methods_by_name)
    SERVICE_NAMES = (
        User_pb2.DESCRIPTOR.services_by_name['User'].full_name,
        reflection.SERVICE_NAME,
        health.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
