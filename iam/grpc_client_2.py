import logging
import ipdb

from google.protobuf.descriptor_pool import DescriptorPool
import grpc
from grpc_reflection.v1alpha import reflection_pb2, reflection_pb2_grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
from grpc_reflection.v1alpha.reflection import ReflectionServicer

from generated_grpc import User_pb2


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("iam-service:50051") as channel:  # the name of the service in the insecure channel
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        desc_pool = DescriptorPool(reflection_db)

        service_desc = desc_pool.FindServiceByName("grpc.reflection.v1alpha.ServerReflection")
        print(f"found Greeter service with name: {service_desc.full_name}")
        for methods in service_desc.methods:
            print(f"found method name: {methods.full_name}")
            input_type = methods.input_type
            print(f"input type for this method: {input_type.full_name}")

        request_desc = desc_pool.FindMessageTypeByName(
            "UserData"
        )
        print(f"found request name: {request_desc.full_name}")


def run2(service_name: str, method_name: str):
    with grpc.insecure_channel("iam-service:50051") as channel:
        stub = reflection_pb2_grpc.ServerReflectionStub(channel)

        # Use reflection to find the 'list' method of the 'User' service
        list_request = reflection_pb2.ServerReflectionRequest(
            file_by_filename=service_name,
            file_containing_symbol=method_name,
        )
        list_response = stub.ServerReflectionInfo(iter([list_request]))

        # Extract the method descriptor
        for response in list_response:
            method_descriptor = None
            if response.file_descriptor_response.file_descriptor_proto:
                for file_proto in response.file_descriptor_response.file_descriptor_proto:
                    for service_proto in file_proto.service:
                        if service_proto.name == service_name:
                            for method_proto in service_proto.method:
                                if method_proto.name == method_name:
                                    method_descriptor = method_proto
                                    break
                            if method_descriptor:
                                break
                    if method_descriptor:
                        break
                if method_descriptor:
                    break

                if not method_descriptor:
                    print(f"Method '{method_name}' not found in service '{service_name}'")
                    return

        # Create a request message and invoke the 'list' method
        list_request = User_pb2.ListRequest()  # Customize request data
        # response = stub.InvokeRpcCall(method_descriptor, list_request.SerializeToString())

        # Handle the response (deserialize the response bytes into ListResponse message)
        return User_pb2.UserData.FromString(response.SerializeToString())


    # run2()
