import sublime
import sublime_plugin

class js_debug_writeCommand(sublime_plugin.TextCommand):
  def run(self, edit, text):
    settings = sublime.load_settings('JSDebug.sublime-settings')
    command = settings.get('command')
    symbol = settings.get('string_symbol')
    # print("pos: " + self.view.sel()[0].begin())
    self.view.insert(edit, self.view.sel()[0].begin(), 'console.debug("' + text + '", ' + text + ');')
