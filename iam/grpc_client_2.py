import logging
import ipdb

from google.protobuf.descriptor_pool import DescriptorPool
import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
from grpc_reflection.v1alpha.reflection import ReflectionServicer


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("iam-service:50051") as channel:  # the name of the service in the insecure channel
        reflection_db = ProtoReflectionDescriptorDatabase(channel)
        services = reflection_db.get_services()
        print(f"found services: {services}")

        desc_pool = DescriptorPool(reflection_db)

        ipdb.set_trace()
        service_desc = desc_pool.FindServiceByName("User")
        print(f"found Greeter service with name: {service_desc.full_name}")
        for methods in service_desc.methods:
            print(f"found method name: {methods.full_name}")
            input_type = methods.input_type
            print(f"input type for this method: {input_type.full_name}")

        request_desc = desc_pool.FindMessageTypeByName(
            "UserData"
        )
        print(f"found request name: {request_desc.full_name}")


def run2():
    import grpc
    from grpc_reflection.v1alpha import reflection_pb2_grpc as _reflection_pb2_grpc
    from grpc_reflection.v1alpha import reflection_pb2 as _reflection_pb2

    channel = grpc.insecure_channel("iam-service:50051")
    stub = _reflection_pb2_grpc.ServerReflectionStub(channel)
    # Ask the server for the list of available services
    list_services_response = stub.ServerReflectionInfo
    ipdb.set_trace()

    # Iterate through the services and their methods
    for service_name in list_services_response.service:
        print(f"Service: {service_name}")
        service_request = descriptor_pb2.ServiceDescriptorProto(name=service_name)
        service_response = stub.FileContainingSymbol(service_request)
        service_descriptor = descriptor_pb2.FileDescriptorProto()
        service_response.file.CopyToProto(service_descriptor)
        pool = descriptor_pool.DescriptorPool()
        pool.Add(service_descriptor)
        service_descriptor = pool.FindServiceByName(service_name)
        for method in service_descriptor.methods:
            print(f"  Method: {method.name}")
            print(f"    Input Type: {method.input_type.name}")
            print(f"    Output Type: {method.output_type.name}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
    # run2()
