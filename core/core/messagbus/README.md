Module to create a class that uses the project's settings to create handlers for the project.

This class for registering the handlers for the project should be a runtime object so that it can be available for
use by the project.

The Server will be the Server object, serving handler (the routes).

<br>Client side will be the instance of the registry that holds all the handlers registered.
<br>The server will be running on separate process, but will be installed on the project.
<br>The server instance will be unique for each project hence making it a microservice reflection object.

Each microservice  (Django project) will have this package installed in its INSTALLED_APPS list, this will  act as a client
for the project to interact with the services.

Each instances of the server object will be served by a separate process (containerized) environment.

<h5>
<u>Tasks in line</u> :
</h5>

1. Create Base class interface for creating Service class, that will be used in registry. <b> <span style="color:green"> DONE </span> </b>
<br><br>
2. Create handlers that will be used by the service to register the service. <b> <span style="color:green"> DONE </span> </b>
<br><br>
3. Create script for running gRPC server in the service container. <b> <span style="color:red"> Not Started </span> </b>
<br><br>
4. Create a client class for the gRPC server, which would be common for all micro services. <b> <span style="color:yellow"> In progress </span> </b> <br><br> 
<br><br>
