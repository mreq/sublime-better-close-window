import sublime
import sublime_plugin

class BetterCloseWindow(sublime_plugin.WindowCommand):
	def run(self):
		# close the project
		if int(sublime.version()) >= 3000:
			self.window.run_command('close_workspace')
		else:
			self.window.run_command('close_project')
		# close the window
		self.window.run_command('close_window')
