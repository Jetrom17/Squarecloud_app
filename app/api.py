from webview import Window, settings

class Api:

    def __init__(self):

        self._settings = settings
        self._settings['ALLOW_DOWNLOADS'] = True
        self._settings['OPEN_EXTERNAL_LINKS_IN_BROWSER'] = False
        self._settings['OPEN_DEVTOOLS_IN_DEBUG'] = False

    def read_cookies(self, window: Window):

        print("Getting Cookies")
        cookies = window.get_cookies()
        for cookie in cookies:

            print(f"\t{cookie}\n")
