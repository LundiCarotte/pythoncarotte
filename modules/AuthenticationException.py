class AuthenticationException(Exception):
    """Exception raised during REST calls when authentication is wrong."""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "Authentication error: {0}".format(self.message)
        else:
            return "Authentication error."