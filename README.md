# Example Ranger Plugin

This plugin adds a command to ranger called `hello_world` which displays the message "Hello world!" as a notification in ranger. It also maps the key-binding `hw` to run this command.

---

The purpose of this plugin is to demonstrate how a plugin for ranger can be constructed that can be installed in multiple ways.

It can be installed in any of the following ways:

1. Installing the repository as a python package with pip (this requires [namespace package plugin](https://github.com/ranger/ranger/pull/2302) support in ranger):
   ```bash
   pip install git+https://github.com/joouha/ranger_plugin_hello_world
   ```
2. Clone the repository to ranger's plugin folder:
   ```bash
   git clone https://github.com/joouha/ranger_plugin_hello_world.git ~/.config/ranger/plugins
   ```
3. Download the file `./ranger_plugins/hello_world/hello_world.py` and copy it to ranger's plugin folder (`~/.config/ranger/plugins`).

---

### Notes

In order to be able to clone the repository to ranger's plugins folder and for ranger to recognise it as a plugin:
- The special `__init__.py` script at the root of the repository is required
- The name of the repository should be a valid python module name
