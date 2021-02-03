# SeedR

**English** | [中文](README_cn.md)

> **Note**: SeedR is developed based on [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged), and **DO NOT** support MCDR v0.x

**SeedR** is a MCDR plugin, which reforged from [White_Paper](https://github.com/AngelicaRoot)/[**Seed**](https://github.com/MCDReforged/Seed) , provide command `!!seed` to get seed of server level like vanilla command `/seed`, and function `get_seed` which can be called by other plugins.

Requires server to enable **`RCON`** connection (Edit `config.yml` of **MCDR instance** and `server.properties` of **server**), reply message like **vanilla** format (with `hoverEvent` and `clickEvent`).

## Installation

### Latest Release

Download latest `SeedR-<version>.zip` from [**Releases Page**](https://github.com/Van-Involution/SeedR/releases) and unzip it, then put `SeedR.py` into `plugins/` directory.

### Latest Source Code

Clone this repository (`git clone`) into `plugins/` directory, then edit `config.yml` of **MCDR instance** as the following codeblock:

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/SeedR
```

## Usages

### Command

Plugin provides cmooand `!!seed` without any parameters to get server seed, reply translated vanilla message with hover text and click-to-copy-seed.

### Function

Plugin defines a callable function:

```Python
def get_seed(server: ServerInterface) -> Union[RTextList, RText]
```

This function returns translated vanilla format seed message (**RText** class). When call this function, please make sure MCDR has **RCON** connection with server in the runtime environment.
