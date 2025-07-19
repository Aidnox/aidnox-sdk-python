# aidnox_sdk/exceptions.py

class AidnoxAPIError(Exception):
    """Base class for all Aidnox API-related exceptions."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

    def __str__(self):
        if self.status_code:
            return f"{self.__class__.__name__} ({self.status_code}): {self.args[0]}"
        return f"{self.__class__.__name__}: {self.args[0]}"


class AuthenticationError(AidnoxAPIError):
    """Raised when the API returns a 401 Unauthorized or similar."""


class RateLimitError(AidnoxAPIError):
    """Raised when the API returns a 429 Too Many Requests."""


class BadRequestError(AidnoxAPIError):
    """Raised when the API returns a 400 Bad Request."""


class NotFoundError(AidnoxAPIError):
    """Raised when the API returns a 404 Not Found."""
