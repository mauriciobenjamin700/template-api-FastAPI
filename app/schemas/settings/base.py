from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base class to be inherited by all schemas.
    
    - Methods:
        - to_dict: Method to convert the model to a dictionary.
    """
    def to_dict(self, exclude: list = [], include: dict = {}, remove_none: str = True) -> dict:
        """
        Method to convert the model to a dictionary.
        
        - Args:
            - exclude: list : A list of fields to exclude from the dictionary.
            - include: dict : A dictionary of fields to include in the dictionary.
            - remove_none: bool : A flag to remove None values from the dictionary.            
        - Returns:
            - dict : A dictionary representation of the model.
        """
        data = self.model_dump()

        for key, value in data.items():
            if key in exclude:
                del data[key]
            if remove_none and value is None:
                del data[key]
                
        data.update(include)

        return data