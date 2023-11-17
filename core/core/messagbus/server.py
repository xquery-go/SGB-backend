from abc import ABC
from abc import abstractmethod

from grpc import server
from concurrent.futures import ThreadPoolExecutor

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     your_proto_file_pb2_grpc.add_YourServiceServicer_to_server(YourService(), server)
#
#     # Enable gRPC reflection
#     SERVICE_NAMES = (
#         your_proto_file_pb2.DESCRIPTOR.services_by_name['YourService'].full_name,
#         reflection.SERVICE_NAME,
#     )
#     reflection.enable_server_reflection(SERVICE_NAMES, server)
#
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     server.wait_for_termination()


class Server:
    __server = None

    def __init__(
            self,
            thread_pool=10,
            handler=None,
            interceptors=None,
            options=None,
            maximum_concurrent_rpcs=None,
            compression=None,
            xds=False,
    ):
        self.thread_pool = thread_pool
        self.handler = handler
        self.interceptors = interceptors
        self.options = options
        self.maximum_concurrent_rpcs = maximum_concurrent_rpcs
        self.compression = compression
        self.xds = xds

    def _server(self):
        if not self.__server:
            self.__server = server(
                thread_pool=ThreadPoolExecutor(self.thread_pool,),
                handlers=self.handler,
                interceptors=self.interceptors,
                options=self.options,
                maximum_concurrent_rpcs=self.maximum_concurrent_rpcs,
                compression=self.compression,
                xds=self.xds,
            )
        return self.__server

    def add_port(self, port, insecure=True):
        if insecure:
            self.__server.add_insecure_port(port)

    def run(self, port):
        self.handler.registry_collection(
            self.__server,
        )
        self.add_port(port)
        self.start_server()

    def start_server(self):
        self.__server.start()
        self.__server.wait_for_termination()


class BaseAbstractService(ABC):
    _servicer = None

    @abstractmethod
    def servicer(self):
        pass

    @abstractmethod
    def get_add_servicer_method(self):
        pass

    @abstractmethod
    def label(self):
        pass


