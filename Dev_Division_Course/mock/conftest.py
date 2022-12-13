import os
import signal
import subprocess
import time
from pathlib import Path

import requests
from requests.exceptions import ConnectionError, ConnectTimeout

import settings
from mocks.surname_mock import run_mock

repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))


def wait_app_ready(timeout=5):
    started = False
    st = time.time()
    while time.time() - st <= timeout:
        try:
            requests.get(f'http://{settings.APP_HOST}:{settings.APP_PORT}/status')
            started = True
            break
        except (ConnectionError, ConnectTimeout):
            pass

    if not started:
        raise RuntimeError(f'App did not started in {timeout}s!')



def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        ################ MOCK CONFIG
        mock = run_mock()
        config.mock = mock
        time.sleep(1)

        ################ STUB CONFIG
        stub_path = Path(repo_root).joinpath('mocks').joinpath('age_stub.py')
        env = os.environ.copy()

        env.update(
            {
                'STUB_HOST': settings.STUB_HOST,
                'STUB_PORT': settings.STUB_PORT
            }
        )

        # stub_path is chmod +x and has shebang line. so we can execute it directly
        stub_proc = subprocess.Popen(stub_path.as_posix(), shell=True,
                                     stdout=open('/tmp/stub_stdout.log', 'w'),
                                     stderr=open('/tmp/stub_stderr.log', 'w'),
                                     env=env
                                     )
        config.stub_proc = stub_proc
        time.sleep(1)

        ################ APP CONFIG
        app_path = Path(repo_root).joinpath('application').joinpath('app.py')

        env = os.environ.copy()
        env.update(
            {
                'APP_HOST': settings.APP_HOST,
                'APP_PORT': settings.APP_PORT,
                'AGE_HOST': settings.STUB_HOST,
                'AGE_PORT': settings.STUB_PORT,
                'SURNAME_HOST': settings.MOCK_HOST,
                'SURNAME_PORT': settings.MOCK_PORT,
            }
        )

        # app_path does not have shebang, execute it by python without shell
        app_proc = subprocess.Popen(['python', app_path.as_posix()],
                                    stdout=open('/tmp/app_stdout.log', 'w'),
                                    stderr=open('/tmp/app_stderr.log', 'w'),
                                    env=env
                                    )

        config.app_proc = app_proc
        wait_app_ready()


def pytest_unconfigure(config):
    if not hasattr(config, 'app_proc') and not hasattr(config, 'stub_proc'):
        return

    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

    config.mock.join()

    config.stub_proc.send_signal(signal.SIGINT)
    config.app_proc.send_signal(signal.SIGINT)
    assert config.app_proc.wait(timeout=5) == 0
