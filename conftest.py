from fixtures.application import Application
import pytest
import jsonpickle
import os


def load_config_from_file(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as cf:
        configuration = jsonpickle.decode(cf.read())
    return configuration


@pytest.fixture
def app(request):
    web_config = load_config_from_file(request.config.getoption("--config"))
    base_url = web_config['base_url']
    fixture = Application(base_url=base_url)
    yield fixture
    fixture.destroy()
    return fixture


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")