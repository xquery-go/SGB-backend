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
    _port = None
    _host = None

    def __init__(
            self,
            thread_pool=10,
            handlers=None,
            interceptors=None,
            options=None,
            maximum_concurrent_rpcs=None,
            compression=None,
            xds=False,
    ):
        self.thread_pool = thread_pool
        self.handlers = handlers
        self.interceptors = interceptors
        self.options = options
        self.maximum_concurrent_rpcs = maximum_concurrent_rpcs
        self.compression = compression
        self.xds = xds

    def _server(self):
        self.__server = server(
            thread_pool=ThreadPoolExecutor(self.thread_pool,),
            handlers=self.handlers,
            interceptors=self.interceptors,
            options=self.options,
            maximum_concurrent_rpcs=self.maximum_concurrent_rpcs,
            compression=self.compression,
            xds=self.xds,
        )
        return self.__server

    def add_port(self, port, insecure=True):
        if insecure:
            if not self._port:
                self._port = port
                self.__server.add_insecure_port(self._port)

    def start_server(self):
        self.__server.start()
        self.__server.wait_for_termination()
