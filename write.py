import sublime
import sublime_plugin

class js_debug_writeCommand(sublime_plugin.TextCommand):
  def run(self, edit, text):
    settings = sublime.load_settings('JSDebug.sublime-settings')
    command = settings.get('command')
    symbol = settings.get('string_symbol')
    self.view.insert(edit, self.view.sel()[0].begin(), 'console.' + command + '(' + symbol + text + symbol + ', ' + text + ');')
