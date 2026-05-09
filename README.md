# YSMParser - GUI Enhanced Edition

这是基于 [OpenYSM/YSMParser](https://github.com/OpenYSM/YSMParser) 的图形化增强分支。

本项目为原版的命令行工具添加了一个现代化的 Python 图形界面 (GUI)，旨在为不熟悉命令行操作的用户提供更便捷的 YSM 模型解密与提取体验。

## ✨ 特性 (Features)

- **一键解析**：无需输入复杂的命令，通过可视化窗口即可完成操作。
- **批量处理**：支持选择整个文件夹，自动扫描并批量提取所有 .ysm 文件。
- **现代化 UI**：采用深色模式设计，具备实时解析日志显示。
- **兼容性**：完美适配 YSM V3 版本的目录解析逻辑。

## 🚀 快速开始 (Quick Start)

1. **环境准备**：
   - 确保你的电脑已安装 [Python 3.10+](https://python.org)。
   - 安装依赖库：`pip install PySide6`

2. **放置核心文件**：
   - 请从 [OpenYSM/YSMParser Releases](https://github.com/OpenYSM/YSMParser/releases) 下载编译好的 `YSMParser.exe`。
   - 将 `YSMParser.exe` 放置在本项目根目录下（即 `main.py` 旁边）。

3. **运行程序**：
   ```bash
   python main.py
