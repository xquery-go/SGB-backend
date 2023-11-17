"""
Basically, this app is installed in all microservices and their duplicates (where the gRPC server is running)
So every microservice is made up of 2 same django projects,
1 is the main application and the other copy runs the management command that runs the gRPC server.

Since in our backend, the applications are run on docker containers, the django project is run in one container
the gRPC server is run in another separate container with same code but a different command during the
build process.

Each  application has its own set of handlers defined in the django conf settings which are
instances of class RegistryCollection and by the name of HANDLER

The services must be of BaseAbstractService class and should be registered in the HANDLER using
register method by giving the service dotted path.

The handler in settings will be required by the gRPC server to serve the request.

So, main application is running on ports starting 8000 (ipv4) and its gRPC server is running  on ports starting
 50051 (ipv6).



 Once the gRPC server is running,
 We need to have a gRPC client that connects to the gRPC server
"""