class ValidationError(Exception):
    """
    A class that represents a validation error.

    - Attributes:
        - status_code: The status code of the error.
        - field: The field that caused the error.
        - detail: The error message.
    """

    def __init__(self, field: str, detail: str):
        """
        The constructor for the ValidationError class.

        - Args:
            - field: The field that caused the error.
            - detail: The error message.
        """
        self.status_code = 422
        self.field = field
        self.detail = detail
        super().__init__(f"{field}: {detail}")