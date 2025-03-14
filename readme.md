# UI Playwright Pet Project

## Описание

Этот проект предназначен для автоматизированного тестирования веб-приложения с использованием Python, Playwright и Pytest.  
Тесты запускаются в GitHub Actions с поддержкой параллельного выполнения (pytest-xdist) и генерацией отчётов в Allure.

## Технологии
- Python 3.11
- Playwright
- Pytest
- Allure
- GitHub Actions (CI/CD)

## Установка и запуск локально:

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/your-username/ui_playwright_pet_project.git
   cd ui_playwright_pet_project
   
2. Установи зависимости:
	```bash
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	playwright install --with-deps
 
3. Запусти тесты локально:
	```bash
	pytest --alluredir=allure-results
 
4. Сгенерируй Allure-отчёт:
	```bash
	allure generate allure-results -o allure-report --clean
	allure open allure-report
 
## Запуск в GitHub Actions

В репозитории настроен GitHub Actions workflow для автоматического запуска тестов.

### Доступные типы тестов:
* Все тесты: запускаются по умолчанию
* Smoke-тесты: можно запустить отдельно

### Ручной запуск через GitHub Actions
1. Перейти в репозиторий → Actions
2. Выбрать Run Tests
3. Нажать Run workflow и выбрать test_type:
* all (все тесты)
* smoke (smoke-тесты)


### Дополнительно
* Параллельное выполнение тестов: включено с флагом -n auto
* Aure-отчёт загружается в GitHub Pages после выполнения тестов - https://skinnycold.github.io/ui_playwright_pet_project/
