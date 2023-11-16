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