import os
import configparser
import git
from datetime import datetime
import graphviz
import pytz
import random

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['settings']

def get_commits(repo_path, commit_date):
    repo = git.Repo(repo_path)
    commits = []
    for commit in repo.iter_commits():
        if commit.committed_datetime > commit_date:
            commits.append(commit)
    return commits

def build_graph(commits, output_file):
    dot = graphviz.Digraph(comment='Git Commit Dependencies')
    author_colors = {} # Словарь для хранения цветов авторов

    for commit in commits:
        author = commit.author.name
        if author not in author_colors:
            # Генерируем случайный цвет, если автора еще нет в словаре
            author_colors[author] = "#%06x" % random.randint(0, 0xFFFFFF)

        dot.node(commit.hexsha, f"{commit.committed_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n{commit.author.name}", fillcolor=author_colors[author], style="filled")
        for parent in commit.parents:
            dot.edge(parent.hexsha, commit.hexsha)

    dot.render(output_file, view=True)
    print(dot.source)


def main():
    config = load_config('config.ini')
    repo_path = config['repo_path']
    output_file = config['output_file']

    commit_date_str = config['commit_date']
    try:
        commit_date = datetime.strptime(commit_date_str, '%Y-%m-%d').replace(tzinfo=pytz.timezone('UTC'))
    except ValueError as e:
        print(f"Ошибка при парсинге даты: {e}")
        return

    commits = get_commits(repo_path, commit_date)
    if not commits:
        print("Нет коммитов после заданной даты.")
        return
    build_graph(commits, output_file)


if __name__ == "__main__":
    main()