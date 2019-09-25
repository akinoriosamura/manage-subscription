class SubsExtractor(object):
    def __init__(self):
        pass

    def extract_default(self):
        """標準で登録されているサブスク情報を取得

        Returns:
            subs_info [dict]: サブスク情報
        """
        subs_info = {
            "name": "NetFlix",
            "price": 1000,
            "pay_day": "0421"
        }

        return subs_info

    def extract_inperson(self):
        pass

    def extract_mail(self):
        pass
