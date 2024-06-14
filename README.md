# o.zelenko
<h2 align="center">Отчет по выполнению задания 2 "Framework. Selenium WebDriver. Tools QA"</h2>
<h5 align="right"><u>Выполнил: Зеленко Ольга Петровна</u></h5>



Всего в проекте разработано четыре автотеста (по четырём тест-кейсам).
Тестовые проверки реализованы с помощью следующих библиотек для тестирования: **pytest, Selenium и pytest-selenium**. 
Для реализации работы с браузером, элементами страниц используется библиотека **Selenium WebDriver**.
В проекте применены фикстуры, паттерн **Page Object и Singleton,  Factory Method** для работы с браузером. 
В проекте реализована возможность задать браузер, в котором будет выполняться тестирование - **Chrome или FireFox**.
Для логирования действий автотестов в проекте используется **логировщик**.
В тест-кейсе №3 реализован **DDT подход и параметризация**.


<u>Для выполнения тестирования было использовано следующее ПО:</u>

* Windows 10 Pro, вер.22H2, сборка ОС 19045.3208
* PyCharm 2022.3.2 (Community Edition) и интерпретатор Python 3.11
* Google Chrome Версия 123.0.6312.106 (Официальная сборка), (64 бит)




<h3 align="center">Состав проекта</h4>


* **requirements.txt** - список зависимостей, требуемых к установке перед запуском тестов

* **utilities\.py** - допфункции, используемые в процессе теста
* **driver\.py** - локальная точка доступа к драйверу
* **data_test\.py** - тестовые данные
* **logger\.py** - логировщик
* **config\.json** - файл с начальными настройками перед тестированием
* **.gitignore** - файл с правилами работы системы контроля версий


* **\_\_init__.py** - файлы, инициализирующий директорию как пакет

* Директория **tests** содержит 4 модуля с автотестами и **conftest\.py** - фикстуры, используемые в проекте

* Директория **pages** содержит описания используемых в тесте вебстраниц
* Директория **framework** содержит описания вебэлементов вебстраниц
* Директория **forms_pages** содержит описание полей вебстраниц
 


Перед запуском тестов требуется установить необходимые библиотеки и **зависимости** командой: 
```
"путь к дикертории"> pip install -r requirements.txt
```

Для запуска тестов требуется в файле config укзаать браузер, в котоом будет выполняться тестирование, **Chrome или FireFox**. Непосредственно запуск тестов производится через файл в IDE "test_... .py" (ПКМ -> Run) или в командной строке:: 
```
"путь к дикертории"> pytest tests\test_1_alerts_demoqa.py
```