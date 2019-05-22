import sublime, sublime_plugin
try:
    from .gitlab import *
except ValueError:
    from gitlab import *


class GitlabRepositoryCommand(GitlabWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(repo.repository_url())
