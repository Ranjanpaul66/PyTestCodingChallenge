import pytest


def test_first_fun() -> None:
    assert 1 == 1


@pytest.mark.skip
def test_should_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_if_fail():
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_if_fail2():
    assert 1 == 1


@pytest.mark.custom
def test_with_custom_mark() -> None:
    pass


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}: {self.stock_symbol}"


# In fixture funiton name sould be same during test the fixture function
@pytest.fixture
def fixture_func() -> Company:
    return Company(name="IBM", stock_symbol="FVRR")


def test_with_fixture(fixture_func: Company) -> None:
    print(f" My Company name os {fixture_func} fom fixture")


@pytest.mark.parametrize("company_name", ["TikTok", "Instagram", "Twitter"])
def test_parametrize(company_name: str) -> None:
    print(f" test with {company_name}")

# for leveling the parametrize test
@pytest.mark.parametrize("company_name", ["TikTok", "Instagram", "Twitter"], ids=["TikTok Test", "Instagram Test", "Twitter test" ])
def test_parametrize2(company_name: str) -> None:
    print(f" test with {company_name}")


