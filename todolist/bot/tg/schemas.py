from pydantic.main import BaseModel


class Chat(BaseModel):
    id: int
    first_name: str or None = None
    username: str or None = None


class Message(BaseModel):
    chat: Chat
    text: str or None = None


class UpdateObj(BaseModel):
    update_id: int
    message: Message or None = None
    edited_message: Message or None = None


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message


class GetUpdatesResponse(BaseModel):
    ok: bool
    result: list[UpdateObj]
