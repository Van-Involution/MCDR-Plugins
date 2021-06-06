# SeedR

[English](README.md) | **中文**

> **注意**：SeedR 基于 [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged) 开发，并且**不支持** MCDR v0.x

**SeedR** 是一个 MCDR 插件，由 [White_Paper](https://github.com/AngelicaRoot)/[**Seed**](https://github.com/MCDReforged/Seed) 重制而成，提供如同原版 `/seed` 命令般获取服务端存档种子的 `!!seed` 命令，以及可供调用的用以获取种子的 `get_seed` 函数。

需要服务端开启 **`RCON`** 连接（编辑 **MCDR 实例**的 `config.yml` 以及**服务端**的 `server.properties`），回复**原版**格式的消息（具有 `hoverEvent` 和 `clickEvent`）。

## 安装插件

### 最新发布

在 [**Releases 页面**](https://github.com/Van-Involution/SeedR/releases)下载最新的 `SeedR-<版本号>.zip`，解压后将 `SeedR.py` 放入 `plugins/` 目录中。

### 最新源码

将仓库克隆（`git clone`）至 `plugins/` 目录中，并按如下代码块编辑 **MCDR 实例**的 `config.yml`：

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/SeedR
```

## 使用插件

### 命令

插件提供无参数的 `!!seed` 命令获取服务端种子，并回复具有悬停文本和单击复制种子功能的经过翻译的消息。

### 函数

插件定义了一个可供引用的函数：

```Python
def get_seed(server: ServerInterface) -> RTextBase:
    ...
```

此函数返回原版格式的经过翻译的种子消息（**RText** 类型）。调用此函数时，请确保运行环境中 MCDR 与服务端的 **RCON** 连接已建立。
