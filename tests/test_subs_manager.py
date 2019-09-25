import pytest

from app import subs_manager


@pytest.fixture
def manager():
    return subs_manager.SubsManager()


def test_extract_subs(manager):
    """インプットに応じたextractorからサブスク取得"""
    # extract_type = "MAIL"
    # extract_type = "INPERSON"
    extract_type = "DEFAULT"
    if extract_type == "DEFAULT":
        subs_info = manager.extract_subs(extract_type)
        assert isinstance(subs_info, dict)
        assert subs_info != {}
