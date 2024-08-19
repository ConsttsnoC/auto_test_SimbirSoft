
<!-- Заголовок -->
<h1 align="center">
  <br>
  Тестовое задание для компании SimbirSoft
  <br>
</h1>
<!-- Описание -->
<p align="center">
  <a href="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" target="_blank">
  </a>
</p>
<!-- Иконки -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-green">
  <img src="https://img.shields.io/badge/Page Object Model-red">
</p>

## Описание проекта

Этот проект представляет собой тестовое задание для компании SimbirSoft. Тесты написаны на Python с использованием подхода Page Object Model (POM). Для логирования используется библиотека `loguru`, а для отчётности тестов используется `allure`. Для форматирования кода использовался `black`. Для распределения и запуска тестов используется `selenium grid + docker`

## Установка

## Предварительные требования

1. **Клонируйте репозиторий используя команду**
    ```bash
      git clone
    ```

2. **Убедитесь, что у вас установлен Python 3.12.3**

   Проверьте версию Python с помощью команды:
   ```bash
   python --version
    ```
3. **Создайте и активируйте виртуальное окружение**
   
   Создайте виртуальное окружение в текущей директории (замените myenv на желаемое имя вашего окружения)
    ```bash
      python -m venv myenv
    ```
    Активируйте виртуальное окружение:
    Для Windows:
    ```bash
     myenv\Scripts\.\activate 
   ```
    Для macOS и Linux: 
   ```bash
     source myenv/bin/activate
    ```
    После активации виртуального окружения вы увидите его имя в начале строки командной строки.

5. **Установите зависимости из requirements.txt**
    
    ```bash
    pip install -r requirements.txt
   ```
        
### Запуска образа Docker Selenium Hub с браузером Chrome
Для запуска используйте команду: 
```bash
docker-compose up -d
   ```

### Запуск тестов Pytest
Для запуска тестов используйте команду: 
```bash
pytest  --reruns 3  --alluredir=allure-results
   ```

## Запуск генерации отчёта allure
```bash
allure serve
 ```

## Для просмотра отчёта allure после запуска docker, можете перейти по:
```bash
http://localhost:4040
 ```
## Запуск тестов локально для Windows
Для включения переменной, Windows: 
```bash
$env:LOCAL_RUN = "true" 
```
Для отключения переменной, Windows: 
```bash
Remove-Item Env:LOCAL_RUN 
```

## Запуск тестов локально для Unix-подобных систем
Для включения переменной, Unix:
```bash
export LOCAL_RUN=true 
```
Для отключения переменной, Unix:
```bash
unset LOCAL_RUN 
```

