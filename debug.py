import sublime
import sublime_plugin

class js_debugCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.active_window().show_input_panel('', '', self.write, lambda *args: None, lambda *args: None)

  def write(self, arg):
    self.view.run_command("js_debug_write", { 'text': arg })

class js_debug_writeCommand(sublime_plugin.TextCommand):
  def run(self, edit, text):
    settings = sublime.load_settings('JSDebug.sublime-settings')
    command = settings.get('command')
    symbol = settings.get('string_symbol')
    self.view.insert(edit, self.view.sel()[0].begin(), 'console.' + command + '(' + symbol + text + symbol + ', ' + text + ');')
