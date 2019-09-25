from app import subs_extractor


class SubsManager(object):
    def __init__(self):
        self.extractor = subs_extractor.SubsExtractor()

    def extract_subs(self, extract_type):
        """extractorを利用しサブスク情報を取得

        Args:
            extract_type ([str]): サブスクリプションの抽出タイプ(DEFAULT, INPERSON, MAILがある)

        Returns:
            subs info [dict]: サブスクリプション情報辞書
        """
        subs_info = {}
        if extract_type == "DEFAULT":
            subs_info = self.extractor.extract_default()

        return subs_info
