import pytest
from krisinformation.crisis_alerter import CrisisAlerter
from krisinformation.const import COUNTY_CODES


def test_news():
    """Test news."""
    alerter = CrisisAlerter(None, "sv")
    news = alerter.news()
    if len(news) == 0:
        pytest.skip("No news available")
    assert len(news[0]["PushMessage"]) > 0
    assert len(news[0]["Published"]) > 0
    if news[0]["Area"][0]["Type"] == "County":
        assert news[0]["Area"][0]["Description"] in COUNTY_CODES.values()
    assert news[0]["Language"] == "sv-SE"

def test_vmas():
    """Test VMA."""
    alerter = CrisisAlerter(None, "sv")
    vmas = alerter.vmas(is_test=True)
    assert len(vmas) > 0
    assert len(vmas[0]["PushMessage"]) > 0
    assert len(vmas[0]["Published"]) > 0
    if vmas[0]["Area"][0]["Type"] == "County":
        assert vmas[0]["Area"][0]["Description"] in COUNTY_CODES.values()
    assert vmas[0]["Language"] == "sv-SE"
