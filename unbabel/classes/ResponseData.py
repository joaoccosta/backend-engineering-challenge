import pandas as pd

class ResponseData:
    """
    Response date contain average delivery_time info for a certain minute
    """

    def __init__(self, timestamp, average_delivery_time):
        """
        Construct a new 'ResponseData' object.

        :param timestamp: The timestamp for the corresponding to the average delivery time
        :param average_delivery_time: The value of average delivery time for the corresponding timestamp
        :return: returns nothing
        """
        self.timestamp = timestamp
        self.average_delivery_time = average_delivery_time

    def getTimestamp(self):
        """
        get timestamp value from ResponseData

        :return: returns a string corresponding to a timestamp
        """
        return self.timestamp

    def getAverageDeliveryTime(self):
        """
                get average_delivery_time value from ResponseData

                :return: returns the value of average_delivery_time, a double
                """
        return self.average_delivery_time

    def __str__(self) -> str:
        """

        :return: a string containing the data from ResponseData
        """
        if self.getAverageDeliveryTime().is_integer():

            #if value is a int, pass the value to int instead of float
            average_to_print = int(self.average_delivery_time)
        else:
            average_to_print = self.average_delivery_time

        str_of_translatiodata = '{'\
            '"date": "' + str(self.getTimestamp()) + '", '\
            '"average_delivery_time": ' + str(average_to_print) + ''\
             '}'


        return str_of_translatiodata
