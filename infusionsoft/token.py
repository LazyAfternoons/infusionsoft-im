import time


class Token:
    """Token class for representing an auth token for the infusionsoft class.
    """

    def __init__(self, access_token, refresh_token, end_of_life, extra_info=None):
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

    def is_expired(self):
        """Checks the expiration date of the token.

        Returns:
            True if the token is expired, false otherwise.
        """
        return int(self.end_of_life) < int(time.time())

    def __str__(self):
        return f'Access Token: {self.access_token}\nRefresh Token: {self.refresh_token}\nEnd Of Life: {self.end_of_life}'


class TokenExpiredException(Exception):
    """Exception thrown when an error related to the token occurs
    """
    pass


