from ..framework.utils.logger import Logger

import pytest
from _pytest.runner import CallInfo


@pytest.fixture(scope="function", autouse=True)
def start_and_finish_test(request):
    Logger.info(f"Start test {request.node.name}")

    yield

    Logger.info(f"Finish test {request.node.name}")


def pytest_exception_interact(node, call: CallInfo, report):
    if report.failed:
        Logger.error(call.excinfo)
