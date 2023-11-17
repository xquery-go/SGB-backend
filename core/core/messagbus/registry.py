"""
Module to create a class that uses the project's settings to create handlers for the project.

This class for registering the handlers for the project should be a runtime object so that it can be available for
use by the project.

The Server will be the Server object, serving handler (the routes).



Client side will be the instance of the registry that holds all the handlers registered.
The servre will be running on separate process, but will be installed on the project.
The server instance will be unique for each project hence making it a microservice reflection object.


To interact with the project and its componenets, the server will use the 'BaseCommand' handle to process requests
such as interacting with the database.
"""
from django.core.management import BaseCommand
import os
from django.utils.module_loading import import_string
from grpc_health.v1 import health_pb2_grpc, health
from grpc_reflection.v1alpha import reflection
from grpc_health.v1.health_pb2 import HealthCheckResponse

# Write a mechanism such that when we install the app it should read the handlers registered,
# and then those handlers should be collected and served


class RuntimeGRPCRegistry:
    """
    The service class must be of Service class instance inherited from BaseAbstractService.
    """
    def __init__(self, service):
        super().__init__()
        self._service_class = import_string(service)

    @property
    def service_class(self):
        return self._service_class

    def register_to_server(self, server):
        return self._service_class.get_add_servicer_method(self.service_class.servicer, server)

    # def service(
    #     self, handler_call_details: grpc.HandlerCallDetails
    # ) -> Optional[grpc.RpcMethodHandler]:
    #     details_method = handler_call_details.method
    #     return self._method_handlers.get(
    #         details_method
    #     )


class RegistryCollection:
    def __init__(self):
        self._registry = set()

    def register(self, service):
        runtime_registry = RuntimeGRPCRegistry(service)
        return self._registry.add(runtime_registry)

    def registry_collection(self, server):
        service_names = [
            reflection.SERVICE_NAME,
            health.SERVICE_NAME,
        ]
        health_servicer = health.HealthServicer(experimental_non_blocking=True)
        health_servicer.set('', HealthCheckResponse.SERVING)

        for service in self._registry:
            service.register(server)
            service_names.append(service.label)
            status = HealthCheckResponse.SERVING
            health_servicer.set(service.label, status)
        health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
        reflection.enable_server_reflection(service_names, server)



