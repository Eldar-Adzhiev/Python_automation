# v.vodopyanov

**To run tests**

cd v.vodopyanov

python -m venv venv
venv\Scripts\activate
cd task1\project_task1
pip install -r requirements.txt

pytest -s -v test_task1.py
or
pytest -s -v --tb=line test_task1.py