import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: russian, english, french, spanish, italian")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture   
def choose_language(language_country):
        if language_country == "ru":
            return "ru"
        elif language_country == "en":
            return "en"
        elif language_country == "fr":
            return "fr"
        elif language_country ==  "es":
            return "es" 
        elif language_country ==  "it":
            return "it"
        assert 0  # чтобы увидеть вывод
    
@pytest.fixture
def language_country(request):
    return request.config.getoption("--language")