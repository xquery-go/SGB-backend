from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloReply(_message.Message):
    __slots__ = ["ReturnGreeting"]
    RETURNGREETING_FIELD_NUMBER: _ClassVar[int]
    ReturnGreeting: str
    def __init__(self, ReturnGreeting: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["Greeting"]
    GREETING_FIELD_NUMBER: _ClassVar[int]
    Greeting: str
    def __init__(self, Greeting: _Optional[str] = ...) -> None: ...
