    def __init__(self):
        self.__option_hover = -1
        self.__option_max = 1
        self.__option_selected = -1

    def get_option_by_hovering(self):
        return self.__option_hover

    def increase_hover(self):
        if self.__option_hover < self.__option_max - 1:
            self.__option_hover += 1

    def decrease_hover(self):
        if self.__option_hover > 0:
            self.__option_hover -= 1

    def get_option_max(self):
        return self.__option_max

    def set_option_max(self, new_max):
        self.__option_max = new_max

    def get_option_selected(self):
        return self.__option_selected

    def set_hover_as_selected(self):
        self.__option_selected = self.__option_hover

    def reset_selection(self):
        self.__option_hover = -1
        self.__option_selected = -1
