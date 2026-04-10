from pydantic import BaseModel, EmailStr


class LeitorBase(BaseModel):
    id: int
    nome: str
    email: EmailStr


class LeitorCreate(LeitorBase):
    pass


class LeitorOut(LeitorBase):
    pass
