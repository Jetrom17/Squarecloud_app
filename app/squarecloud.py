from webview import start, create_window
from .api import Api


class SquareCloudApp:

    """Square Cloud App"""

    def __init__(self, *, width: int=1280, height: int=720):

        self._api = Api()
        self._width, self._height = width, height
        self.window = create_window(
            title="Square Cloud",
            url="https://squarecloud.app",
            js_api=self._api,
            width=self._width,
            height=self._height,
            confirm_close=True,
        )

    def run(self):

        print("Running app")
        start(self._api.read_cookies, self.window, private_mode=False, user_agent='Chrome/128.0.0.0')