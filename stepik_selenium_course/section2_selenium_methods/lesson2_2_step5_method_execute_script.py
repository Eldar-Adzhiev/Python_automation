"""
С помощью метода execute_script можно выполнить программу, написанную на языке
JavaScript, как часть сценария автотеста в запущенном браузере.
"""

# Давайте попробуем вызвать alert в браузере с помощью WebDriver.
# Пример сценария:
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")

"""
Обратите внимание, что исполняемый JavaScript нужно заключать в кавычки 
(двойные или одинарные). Если внутри скрипта вам также понадобится 
использовать кавычки, а для выделения скрипта вы уже используете двойные 
кавычки, то в скрипте следует поставить одинарные:
"""
# browser.execute_script("document.title='Script executing';")

"""
Такой формат записи тоже будет работать:
"""
# browser.execute_script('document.title="Script executing";')

"""
Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив
их через точку с запятой. Изменим сначала заголовок страницы, а затем 
вызовем alert:
"""
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

"""
Для клика в WebDriver мы используем метод click(). Если элемент оказывается 
перекрыт другим элементом, то наша программа вызовет следующую ошибку

Чтобы увидеть пример данной ошибки, запустите следующий скрипт:
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()

"""
Если мы столкнулись с такой ситуацией, мы можем заставить браузер 
дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
Делается это с помощью следующего скрипта:
"return arguments[0].scrollIntoView(true);"

В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие 
команды в коде:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

"""
В метод execute_script мы передали текст js-скрипта и найденный элемент button,
к которому нужно будет проскроллить страницу. После выполнения кода элемент 
button должен оказаться в верхней части страницы. Подробнее о методе см 
https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView .

Также можно проскроллить всю страницу целиком на строго заданное количество 
пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:

browser.execute_script("window.scrollBy(0, 100);")
!Важно. Мы не будем в этом курсе изучать, как работает JavaScript, и 
обойдемся только приведенным выше примером скрипта с прокруткой страницы. 
Для сравнения приведем скрипт на этом языке, который делает то же, что 
приведенный выше пример для WebDriver:

// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);
Можете попробовать исполнить его в консоли браузера на странице 
http://suninjuly.github.io/execute_script.html. Для этого откройте инструменты разработчика в браузере, перейдите на вкладку консоль (console), скопируйте туда этот код и нажмите Enter. Таким образом можно протестировать кусочки js кода прежде чем внедрять его в свои тесты на python. 

Обратите внимание, что в коде в WebDriver нужно использовать ключевое слово 
return. Также его нужно будет использовать, когда вы захотите получить 
какие-то данные после выполнения скрипта. При этом при тестировании скрипта 
в консоли браузера слово return использовать не надо.
"""
