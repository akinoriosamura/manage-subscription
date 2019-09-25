import pytest

from app import subs_extractor


@pytest.fixture
def extractor():
    return subs_extractor.SubsExtractor()


def test_extract_default(extractor):
    subs_info = extractor.extract_default()
    assert isinstance(subs_info, dict)
    assert subs_info != {}
