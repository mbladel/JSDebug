import sublime
import sublime_plugin

class js_debugCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.active_window().show_input_panel('boh', '', self.write, lambda *args: None, lambda *args: None)

  def write(self, arg):
    self.view.run_command("js_debug_write", { 'text': arg })
