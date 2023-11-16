from grpc import server
from concurrent.futures import ThreadPoolExecutor


class Server:
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

    def _run(self):
        return server(ThreadPoolExecutor(self.thread_pool))
