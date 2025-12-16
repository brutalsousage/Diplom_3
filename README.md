project_root/
├── README.md
├── .gitignore
├── help/
│   ├── __init__.py
│   ├── data.py
│   ├── urls.py
│   └── wait_assistant.py
├── locators/
│   ├── __init__.py
│   ├── login_page_locators.py
│   ├── main_page_locators.py
│   ├── order_feed_locators.py
│   └── order_modal_locators.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── order_feed_page.py
│   └── order_modal_page.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_main.py
    └── test_order.py


Проверка основной функциональности:
переход по клику на «Конструктор»;
переход по клику на раздел «Лента заказов»;
если кликнуть на ингредиент, появится всплывающее окно с деталями;
всплывающее окно закрывается кликом по крестику;
при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.

Раздел «Лента заказов»:
при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
после оформления заказа его номер появляется в разделе «В работе».
