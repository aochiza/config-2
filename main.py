import os
import configparser
import git
from datetime import datetime
import graphviz
import pytz #

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

def build_graph(commits):
    dot = graphviz.Digraph(comment='Git Commit Dependencies')
    for commit in commits:
        dot.node(commit.hexsha, f"{commit.committed_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n{commit.author.name}")
        for parent in commit.parents:
            dot.edge(parent.hexsha, commit.hexsha)
    return dot

def main():
    config = load_config('config.ini')
    graphviz_path = config['graphviz_path']
    repo_path = config['repo_path']
    output_file = config['output_file']

    # Изменение здесь: добавляем часовой пояс
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
    dot = build_graph(commits)
    dot.render(output_file, view=True)
    print(dot.source)

if __name__ == "__main__":
    main()