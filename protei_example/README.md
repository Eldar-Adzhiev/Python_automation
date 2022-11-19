To run tests

cd v.vodopyanov/task3

python -m venv venv 

venv\Scripts\activate 

pip install -r requirements.txt

cd tests

pytest -s -v test_task3.py 

or 

pytest -s -v --tb=line test_task3.py