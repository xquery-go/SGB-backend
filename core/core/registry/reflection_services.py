from concurrent import futures
import grpc
import grpc_reflection.v1alpha.reflection as reflection


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    your_proto_file_pb2_grpc.add_YourServiceServicer_to_server(YourService(), server)

    # Enable gRPC reflection
    SERVICE_NAMES = (
        your_proto_file_pb2.DESCRIPTOR.services_by_name['YourService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
