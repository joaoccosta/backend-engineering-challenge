from unbabel.handlers.InputHandler import *

from unbabel.classes.TranslationData import *
from unbabel.classes.ResponseData import *
import sys
import pandas as pd
import numpy as np
from datetime import timedelta

def main(argvs):
    """
    will run the necessary code
    :param argvs:
    :return bool:
    """

    translations = []
    data_parsed = parseInput(argvs)

    for data in data_parsed.data:

        #add a TranslationData for each line in the file inserted by the user
        translations.append(TranslationData(data))


    #get the data in the correct format with the correct values
    responses = getAverege(translations, data_parsed.window_size)

    #print the expected output
    output(responses)

    return True


def getAverege(translations: list, window_size: int) -> list:
    """
    Get average delivery time to each minute
    :param translations:
    :param window_size:
    :return a list of ResponseData:
    """

    first_timestamp_registered = pd.to_datetime(translations[0].getTimestamp()).round('min')
    last_timestamp_registered = pd.to_datetime(translations[-1].getTimestamp()).round('min') + timedelta(minutes=1)

    date_range = pd.date_range(first_timestamp_registered, last_timestamp_registered, freq="1min")
    responses = []
    for date in date_range:

        translation_data = getTranslationsByRangeDate(date, window_size, translations)
        average_delivery_time = getAveregeDeliveryTime(translation_data)

        responses.append(ResponseData(date, average_delivery_time))

    return responses

def getAveregeDeliveryTime(translation_data):
    """
    Get average delivery time for a list of TranslationData
    :param a list of TranslationData:
    :return a float with the value corresponding to the average time of delivery:
    """

    #if no data
    if (len(translation_data) > 0):

        average_delivery_time = np.mean([td.getDuration() for td in translation_data])
    else:
        average_delivery_time = 0.0

    return average_delivery_time



def getTranslationsByRangeDate(date, window_size, translations):
    """
    filters a list by the corresponding value of timestamp and window size
    :param date:
    :param window_size:
    :param translations:
    :return list of TranslationData:
    """
    return list(filter(lambda td: date - timedelta(minutes=window_size) < td.getTimestamp() < date, translations))



def output(responses: list):
    """
    print the expected result
    :param responses:
    :return:
    """
    for response in responses:
        print(response.__str__())





if __name__ == '__main__':
    main(sys.argv)

def run():
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        print("unexpected problem")
        sys.exit(0)

