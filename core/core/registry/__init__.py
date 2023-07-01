import grpc
from grpc_reflection.v1alpha import reflection

# Microservice 1
thread_pool_size = 10
server_microservice1 = grpc.server(thread_pool_size)
reflection.enable_server_reflection('your_service_name_microservice1', server_microservice1)

# Add your services for Microservice 1 to the server
# server_microservice1.add_your_service(your_service_implementation_microservice1)
server_address_microservice1 = 'localhost:50051'  # Replace with your desired server address for Microservice 1
server_microservice1.add_insecure_port(server_address_microservice1)
server_microservice1.start()

# Microservice 2
server_microservice2 = grpc.server(thread_pool_size)
reflection.enable_server_reflection('your_service_name_microservice2', server_microservice2)

# Add your services for Microservice 2 to the server
# server_microservice2.add_your_service(your_service_implementation_microservice2)

server_address_microservice2 = 'localhost:50052'  # Replace with your desired server address for Microservice 2
server_microservice2.add_insecure_port(server_address_microservice2)
server_microservice2.start()

# Run both servers
try:
    while True:
        pass
except KeyboardInterrupt:
    server_microservice1.stop(0)
    server_microservice2.stop(0)
