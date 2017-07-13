# JSDebug

This is a plugin for sublime text that automates console output in Javascript.
After running the command, insert the name of the object you want to output to the console and the plugin will write a "console.method('object', object);" statement.

![gif](http://i.imgur.com/UAUNboU.gif)

# Settings

You can access the settings from Preferences > Package Settings > JSDebug > Settings
- command: the console command to use (ex. log, debug, warn)
- string_symbol: the symbol of choice when writing strings (" or ')

# Keybindings

You can customize the key bindings from Preferences > Package Settings > JSDebug > Key Bindings (User)