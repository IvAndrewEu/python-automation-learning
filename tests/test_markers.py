import pytest
import sys

@pytest.mark.smoke
@pytest.mark.api
def test_login():
    assert True

@pytest.mark.smoke
def test_logout():
    assert True

@pytest.mark.regression
@pytest.mark.api
def test_profile():
    assert True

@pytest.mark.regression
def test_settings():
    assert True

@pytest.mark.skip(reason="Payment service is not ready")
def test_payment():
    assert True

@pytest.mark.skipif(
    sys.platform == "linux",
    reason = "Test works only on Linux"
)
def test_linux_only():
    assert True

@pytest.mark.xfail(reason = "Know bug")
def test_know_bug():
    assert 2 + 2 == 5

@pytest.mark.xfail(reason = "Know bug")
def test_fixed_bug():
    assert 2 + 2 == 4