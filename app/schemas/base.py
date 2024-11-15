from pydantic import BaseModel


class BaseSchema(BaseModel):

    def dict(self) -> dict:
        data = self.model_dump()

        clean = {key: value for key, value in data.items() if value is not None}

        return clean