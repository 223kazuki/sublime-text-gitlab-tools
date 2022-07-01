# GitLab Tools for Sublime Text #

## Introduction ##

A port of temochka's [Github Tools](https://github.com/temochka/sublime-text-2-github-tools) plugin to GitLab.

## Usage ##

Open any directory of your GIT working copy in Sublime Text.

* Press `Ctrl + Shift + P` and select `GitLab: Open File` or just press `Ctrl + Shift + ^` to open currently edited file on GitLab.
* Press `Ctrl + Shift + P` and select `GitLab: Blame` to open blame for currently edited file on GitLab.
* Press `Ctrl + Shift + P` and select `GitLab: History` to open commit history for currently edited file on GitLab.
* Press `Ctrl + Shift + P` and select `GitLab: Copy Link To File` to save a GitLab link to a selected code fragment in the system clipboard.
* Press `Ctrl + Shift + P` and select `GitLab: Repository` to open repository page on GitLab.
* Press `Ctrl + Shift + P` and select `GitLab: Issues` to open repository issues page on GitLab.

Use `Cmd` instead of `Ctrl` on Mac OS X.

## Get it installed ##

### On Mac ###

```bash
cd ~/Library/Application\ Support/Sublime\ Text/Packages/
git clone git://gitlab.com/theoretick/sublime-text-gitlab-tools.git
```

### On Linux ###

```bash
cd ~/.config/sublime-text-3/Packages/
git clone git://gitlab.com/theoretick/sublime-text-gitlab-tools.git
```

### On Windows ###

```
cd %APPDATA%/Sublime Text 3/Packages/
git clone git://gitlab.com/theoretick/sublime-text-gitlab-tools.git
```

Make sure you have included all required binaries (`git`) in your PATH.
