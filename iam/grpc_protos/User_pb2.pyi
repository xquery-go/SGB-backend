from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TokenVerificationRequest(_message.Message):
    __slots__ = ["Token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    Token: str
    def __init__(self, Token: _Optional[str] = ...) -> None: ...

class UserData(_message.Message):
    __slots__ = ["EmailAddress", "UserId", "UserName"]
    EMAILADDRESS_FIELD_NUMBER: _ClassVar[int]
    EmailAddress: str
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    UserName: str
    def __init__(self, UserId: _Optional[int] = ..., UserName: _Optional[str] = ..., EmailAddress: _Optional[str] = ...) -> None: ...

class UserRetrieveRequest(_message.Message):
    __slots__ = ["UserId"]
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...
