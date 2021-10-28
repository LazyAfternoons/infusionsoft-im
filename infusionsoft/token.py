from datetime import time


class Token:
    """Token class for representing an auth token for the infusionsoft class.
    """

    def __init__(self, access_token: str, refresh_token: str, end_of_life: str, extra_info=None):
        """Creates a new Token object.

        Args:
            access_token: Access token generated from infusionsoft.
            refresh_token: Refresh token generated from infusionsoft.
            end_of_life: End of life of the token in unix time.
            extra_info: List of extra info.
        """
        if access_token and refresh_token:
            self.access_token = access_token
            self.refresh_token = refresh_token
            self.end_of_life = end_of_life
            self.extra_info = extra_info
        else:
            raise TypeError("Both access token and refresh token must be provided.")

    def is_expired(self) -> bool:
        """Checks the expiration date of the token.

        Returns:
            True if the token is expired, false otherwise.
        """
        return self.end_of_life < str(time())


class TokenExpiredException(Exception):
    """Exception thrown when an error related to the token occurs
    """
    pass


