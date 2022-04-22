class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method that initializes the TV's default settings.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to turn the TV on/off.
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to turn the channel up.
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to turn the channel down.
        """
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to raise the volume by 1.
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to lower the volume by 1.
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return the TV status in the form of a string.
        :return: TV status as a string.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
