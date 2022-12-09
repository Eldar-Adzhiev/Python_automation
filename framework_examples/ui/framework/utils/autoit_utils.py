import autoit

from ..utils.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()


class AutoItUtils:
    def __init__(self):
        self.wait_timeout = CONFIG['autoit_wait_sec']

    def upload_image(self, window_handle, path_to_file):
        autoit.win_wait_active(window_handle, self.wait_timeout)
        autoit.control_focus(window_handle, "")
        autoit.control_set_text(window_handle, "Edit1", path_to_file)
        autoit.control_click(window_handle, "Button1")
        autoit.win_wait_not_active(window_handle, self.wait_timeout)
