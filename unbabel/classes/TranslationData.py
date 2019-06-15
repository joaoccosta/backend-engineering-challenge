import pandas as pd

class TranslationData:

    def __init__(self, data: dict):
        """
        Construct a new 'TranslationData' object.

        :param data: dictionary that will be parsed to TranslationData, each key of the dictionary will become an attribute of TranslationData
        :return: returns nothing
        """
        for key, value in data.items():
            setattr(self, key, value)


    def getDuration(self):
        """
        Ensures the duration value of TranslationData, if duration is not defined 0.0 will be returned
        :return: a float
        """
        if hasattr(self, 'duration') or self.duration != None:
            return float(self.duration)
        return float(0)

    def getTimestamp(self):
        """
        Ensures the timestamp value of TranslationData, if timestamp is not defined None will be returned
        """
        if hasattr(self, 'timestamp'):
            return pd.to_datetime(self.timestamp)
        return None

    def getTranslationId(self):
        """
        Ensures the translation_id value of TranslationData, if translation_id is not defined None will be returned
        """
        if hasattr(self, 'translation_id'):
            return self.translation_id

        return None

    def getSourceLanguage(self):
        """
        Ensures the source_language value of TranslationData, if source_language is not defined None will be returned
        """
        if hasattr(self, 'source_language'):
            return self.source_language

        return None

    def getTargetLanguage(self):
        """
        Ensures the translation_language value of TranslationData, if translation_language is not defined None will be returned
        """
        if hasattr(self, 'translation_language'):
            return self.translation_language

        return None

    def getClientName(self):
        """
        Ensures the client_name value of TranslationData, if client_name is not defined None will be returned
        """
        if hasattr(self, 'client_name'):
            return self.client_name

        return None

    def getEventName(self):
        """
        Ensures the event_name value of TranslationData, if event_name is not defined None will be returned
        """
        if hasattr(self, 'event_name'):
            return self.event_name

    def getNrWords(self):
        """
        Ensures the nr_words value of TranslationData, if nr_words is not defined None will be returned
        """
        if hasattr(self, 'nr_words'):
            print(self.nr_words)
            return self.nr_words

        return self.nr_words


    def __str__(self) -> str:
        """

        :return: a string containing the data from TranslationData
        """
        str_of_translatiodata = '{'\
            'timestamp: "' + str(self.getTimestamp()) + '", '\
            'translation_id: "' + str(self.getTranslationId()) + '", '\
            'source_language: "' + str(self.getSourceLanguage()) + '", '\
            'target_language: "' + str(self.getTargetLanguage()) + '", '\
            'client_name: "' + str(self.getClientName()) + '" '\
            'event_name: "' + str(self.getEventName()) + '", '\
            'duration: "' + str(self.getDuration()) + '", '\
            'nr_words: "' + str(self.getNrWords()) + '"}'


        return str_of_translatiodata
