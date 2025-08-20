from pydantic import BaseModel

class csModel(BaseModel):
    """
    Chat Question Payload
    """
    question: str