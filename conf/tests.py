import unittest
import configparser
from datetime import datetime
import git
from unittest.mock import patch, MagicMock
import graphviz
import pytz
import os

from main import load_config, get_commits, build_graph

class TestMain(unittest.TestCase):

    def test_load_config(self):
        # Создаем временный файл конфигурации
        config_file = "test_config.ini"
        with open(config_file, "w") as f:
            f.write("[settings]\ngraphviz_path = C:/Program Files/Graphviz/bin/dot.exe\nrepo_path = C:/Users/ksen/conf/.git\ntest_output_file =test_output.dot\ncommit_date = 2022-01-01")

        config = load_config(config_file)
        self.assertEqual(config['graphviz_path'], 'C:/Program Files/Graphviz/bin/dot.exe')
        self.assertEqual(config['repo_path'], 'C:/Users/ksen/conf/.git')
        self.assertEqual(config['test_output_file'], 'test_output.dot')
        self.assertEqual(config['commit_date'], '2022-01-01')
        os.remove(config_file)

    @patch('main.git.Repo')
    def test_get_commits_empty(self, MockRepo):
        MockRepo.return_value.iter_commits.return_value = []
        commit_date = datetime(2024, 10, 27, tzinfo=pytz.UTC)
        commits = get_commits("test_repo", commit_date)
        self.assertEqual(len(commits), 0)

    @patch('main.graphviz.Digraph')
    def test_build_graph_empty(self, MockDigraph):
        commits = []
        MockDigraph.return_value = None
        dot = build_graph(commits)
        self.assertIsNone(dot)

    @patch('main.git.Repo')
    def test_get_commits_some(self, MockRepo):
        mock_commits = [
            MagicMock(committed_datetime=datetime(2024, 10, 27, tzinfo=pytz.UTC), hexsha="commit2",
                      author=MagicMock(name="Author 2"), parents=[MagicMock(hexsha="commit1")]),
            MagicMock(committed_datetime=datetime(2024, 10, 26, tzinfo=pytz.UTC), hexsha="commit1",
                      author=MagicMock(name="Author 1"), parents=[]),
        ]
        MockRepo.return_value.iter_commits.return_value = mock_commits
        commit_date = datetime(2024, 10, 25, tzinfo=pytz.UTC)  # Изменено на более раннюю дату
        commits = get_commits("test_repo", commit_date)
        self.assertEqual(len(commits), 2)  # Ожидаем 2 коммита
        self.assertEqual(commits[0].hexsha, "commit2")
        self.assertEqual(commits[1].hexsha, "commit1")



if __name__ == '__main__':
    unittest.main()