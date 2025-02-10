class DriverNotInitializedError(Exception):
    """Exception raised when the driver is not initialized."""

    def __init__(
        self, message="Driver not initialized. Call `initialize_driver` first."
    ):
        self.message = message
        super().__init__(self.message)


class PageLoadTimeoutError(Exception):
    """Exception raised when a page fails to load within the specified time."""

    def __init__(self, url, message="Page load timeout occurred."):
        self.url = url
        self.message = f"{message} URL: {url}"
        super().__init__(self.message)
