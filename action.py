class Choice:
    """
    Get menu choice from user and validate
    :param option: The menu choice, can be a number 1-6
    """
    def __init__(self, option):
        self.option = option

    def validate_choice(self):
        """
        Convert choice to int, raise exception if wrong option or can't be converted
        :return: True if passes, False if except
        """
        try:
            if int(self.option) > 6:
                raise ValueError(
                    f"Please choose a number between 0 and 6! You provided {self.option}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again. \n")
            return False
        self.option = int(self.option)
        return True


class User:
    def __init__(self, **kwargs):
        self.amazon_url = kwargs["amazon"]
        self.argos_url = kwargs["argos"]
        self.currys_url = kwargs["currys"]


