# Конфигурационное управление. Домашнее задание
# Hi there, I'm [ksen](https://daniilshat.ru/) ![](https://github.com/blackcater/blackcater/raw/main/images/Hi.gif) 
### Задание №2, 2 вариант
### Постановка задачи:
Разработать инструмент командной строки для визуализации графа 
зависимостей, включая транзитивные зависимости. Сторонние средства для 
получения зависимостей использовать нельзя. 
Зависимости определяются для git-репозитория. Для описания графа 
зависимостей используется представление Graphviz. Визуализатор должен 
выводить результат на экран в виде кода.

Построить граф зависимостей для коммитов, в узлах которого содержатся 
дата, время и автор коммита. Граф необходимо строить только для коммитов позже заданной даты. <br />
Конфигурационный файл имеет формат ini и содержит: <br />
• Путь к программе для визуализации графов. <br />
• Путь к анализируемому репозиторию. <br />
• Путь к файлу-результату в виде кода. <br />
• Дата коммитов в репозитории. <br />
Все функции визуализатора зависимостей должны быть покрыты тестами
### Команда для запуска main.py
```
python main.py
```
### Команда для запуска tests.py
```
python tests.py
```
### Содердание ini файла(был изменен для выполнения доп задания)
```
[settings]
graphviz_path = C:\Program Files\Graphviz\bin\dot.exe
repo_path = C:\Users\ksen\conf\logfire\.git
output_file = output_2.gv
commit_date = 2022-01-01
```
### Содержание output.dot
```
// Git Commit Dependencies
digraph {
	"743fb5d720ffa8b6b99d3f53a56d54bf10c5d8d5" [label="2024-12-05 17:04:26
Alex Hall" fillcolor="#f5a6cd" style=filled]
	"4e4620bfc17efb53d3b07162d0b4a9462c85c07d" -> "743fb5d720ffa8b6b99d3f53a56d54bf10c5d8d5"
	"4e4620bfc17efb53d3b07162d0b4a9462c85c07d" [label="2024-12-05 16:59:17
Alex Hall" fillcolor="#f5a6cd" style=filled]
	"3a70878f7ed25efa62874837aee690799ea00257" -> "4e4620bfc17efb53d3b07162d0b4a9462c85c07d"
	"3a70878f7ed25efa62874837aee690799ea00257" [label="2024-12-05 15:54:59
......
```
### Результат тестов main.py
![image](https://github.com/user-attachments/assets/8ff689d1-67ef-43b3-8858-2fe920d6e936)
### Результат тестов tests.py
![image](https://github.com/user-attachments/assets/646453ac-dcd4-42d2-ac98-0bf0beb44d46)

