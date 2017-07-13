import sublime
import sublime_plugin

class js_debug_bothCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.active_window().show_input_panel('', '', self.write, lambda *args: None, lambda *args: None)

  def write(self, text):
    self.view.run_command('js_debug_write', { 'mode': 'both', 'text': text })

class js_debug_messageCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.active_window().show_input_panel('', '', self.write, lambda *args: None, lambda *args: None)

  def write(self, text):
    self.view.run_command('js_debug_write', { 'mode': 'message', 'text': text })

class js_debug_objectCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.active_window().show_input_panel('', '', self.write, lambda *args: None, lambda *args: None)

  def write(self, text):
    self.view.run_command('js_debug_write', { 'mode': 'object', 'text': text })

class js_debug_writeCommand(sublime_plugin.TextCommand):
  def run(self, edit, mode, text):
    settings = sublime.load_settings('JSDebug.sublime-settings')
    command = settings.get('command')
    symbol = settings.get('string_symbol')
    message = 'console.' + command + '('
    print(mode)
    if mode == 'both':
      message += symbol + text + symbol + ', ' + text
    elif mode == 'message':
      message += symbol + text + symbol
    elif mode == 'object':
      message += text
    message += ');'
    for region in self.view.sel():
    	self.view.erase(edit, region)
    	self.view.insert(edit, region.begin(), message)
