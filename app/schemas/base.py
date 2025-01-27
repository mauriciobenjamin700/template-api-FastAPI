from pydantic import BaseModel


class BaseSchema(BaseModel):

    def dict(self, exclude: list = [], **kwargs) -> dict:
        data = self.model_dump()

        clean = {
            key: value 
            for key, value in data.items() 
            if (
                value is not None
                and key not in exclude
            )
        }
        
        for key, value in kwargs.items():
            if key not in clean:
                clean[key] = value

        return clean