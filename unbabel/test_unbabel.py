import unittest
import pandas as pd
import os
from unbabel import unbabel_cli

class TestUnbabel(unittest.TestCase):
    """
        Class that ensure test quality
    """

    def test_main(self):
        """
        test if main class is workig

        :return: returns nothing
        """

        self.assertTrue(unbabel_cli.main(["file.py", "-i", os.path.dirname(os.path.realpath(__file__)) + "/resources/events.json", "-w", "10"]))

    def test_average_delivery_time(self):
        """
                test if average delivery time result is correct

                :return: returns nothing
                """
        test_translations = []
        self.assertEqual(unbabel_cli.getAveregeDeliveryTime(test_translations), 0.0)

        test_translations.append(unbabel_cli.TranslationData(
            {"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5",
             "source_language": "en", "target_language": "fr", "client_name": "easyjet",
             "event_name": "translation_delivered", "nr_words": 30, "duration": 20}))
        self.assertEqual(unbabel_cli.getAveregeDeliveryTime(test_translations), 20.0)

        test_translations.append(unbabel_cli.TranslationData(
            {"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5",
             "source_language": "en", "target_language": "fr", "client_name": "easyjet",
             "event_name": "translation_delivered", "nr_words": 30, "duration": 50}))

        self.assertEqual(unbabel_cli.getAveregeDeliveryTime(test_translations), 35.0)

    def test_filter_translations_by_date(self):
        """
                test if filter translations by date is working

                :return: returns nothing
                """

        test_translations = []

        self.assertEqual(unbabel_cli.getTranslationsByRangeDate(pd.to_datetime("2018-12-26 18:23:19.903159").round('min'), 10, test_translations), [])

        test_translations.append(unbabel_cli.TranslationData(
            {"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5",
             "source_language": "en", "target_language": "fr", "client_name": "easyjet",
             "event_name": "translation_delivered", "nr_words": 30, "duration": 20}))
        self.assertEqual(unbabel_cli.getAveregeDeliveryTime(test_translations), 20.0)

        test_translations.append(unbabel_cli.TranslationData(
            {"timestamp": "2018-12-26 18:50:08.509654", "translation_id": "5aa5b2f39f7254a75aa5",
             "source_language": "en", "target_language": "fr", "client_name": "easyjet",
             "event_name": "translation_delivered", "nr_words": 30, "duration": 50}))

        self.assertEqual(len(unbabel_cli.getTranslationsByRangeDate(pd.to_datetime("2018-12-26 18:13:19.903159").round('min'), 10, test_translations)), 1)


if __name__ == '__main__':
    unittest.main()