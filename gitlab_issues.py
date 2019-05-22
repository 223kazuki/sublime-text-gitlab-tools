import sublime, sublime_plugin
try:
    from .gitlab import *
except ValueError:
    from gitlab import *


class GitlabIssuesCommand(GitlabWindowCommand):
    @with_repo
    def run(self, repo):
        open_url(repo.issues_url())
