BetterCloseWindow
=================

I got fed up with Sublime opening the last project and a new window when closed and being launched. This super-simple plugin offers a single `better_close_window` command, which closes the project and then the window.

Default keybinding is set to override the default `close_window` command.

## Before

1. Work on a `foo.sublime-project`.
2. Close sublime
3. Start sublime opening a folder/project. `subl ~/bar`
4. Two sublime windows open - first with the `foo` project, second with `~/bar` folder.

## Now

1. Work on a `foo.sublime-project`.
2. Close sublime via this plugin
3. Start sublime opening a folder/project. `subl ~/bar`
4. A single sublime window opens - with `~/bar` folder.
