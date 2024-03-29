import sublime, sublime_plugin
try:
    from .gitlab import *
except ValueError:
    from gitlab import *


class GitlabBlameCommand(GitlabWindowCommand):
    @require_file
    @with_repo
    def run(self, repo):
        url = repo.blame_file_url(self.relative_filename())
        view = sublime.active_window().active_view()

        line_begin = view.rowcol(view.sel()[0].begin())[0] + 1
        line_end = view.rowcol(view.sel()[0].end())[0] + 1
        url += '#L%d' % line_begin
        if line_begin != line_end:
            url += '-L%d' % line_end

        open_url(url)
