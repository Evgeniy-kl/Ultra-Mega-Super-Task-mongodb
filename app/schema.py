from pydantic import BaseModel


class Statistic(BaseModel):
    count: int
    email: str
