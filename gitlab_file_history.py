import sublime, sublime_plugin
try:
    from .gitlab import *
except ValueError:
    from gitlab import *


class GitlabFileHistoryCommand(GitlabWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        open_url(repo.file_history_url(self.relative_filename()))
