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


# Write a mechanism such that when we install the app it should read the handlers registered,
# and then those handlers should be collected and served


class RuntimeGRPCRegistry(BaseCommand):
    def __init__(self, service):
        super().__init__()
        self.service = service


class RegistryCollection:
    def __init__(self):
        self._registry = set()

    def register(self, service):
        return self._registry.add(RuntimeGRPCRegistry(service))



