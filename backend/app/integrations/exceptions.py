class IntegrationError(Exception):
    pass

class TokenMissingError(IntegrationError):
    pass

class AuthenticationError(IntegrationError):
    pass
class APIRequestError(IntegrationError):
    pass