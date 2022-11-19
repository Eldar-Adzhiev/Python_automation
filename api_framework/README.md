# protei.testing_api_nominatim
Задача

Написать DDT (data driven tests) тесты публичного API геокодинга https://nominatim.openstreetmap.org/ui/search.html (проект nominatim).

Протестировать необходимо прямое (адрес -> координаты) и обратное (координаты -> адрес) геокодирование. Предпочтительные языки разработки: python (pytest)



To run tests

python -m venv venv

venv\Scripts\activate

pip install -r protei_testing_api_nominatim\requirements.txt

pytest -s -v protei_testing_api_nominatim\tests\test.py

python -m pytest -s -v protei_testing_api_nominatim\tests\test.py
