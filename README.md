# ASCII Gradient Art / ASCII 渐变艺术字

[English](#english) | [中文](#中文)

---

## English

### 🎨 Overview

ASCII Gradient Art is a powerful command-line tool that generates beautiful ASCII art with customizable gradient colors and animations. Transform any text into stunning visual art with various fonts, color themes, and rendering modes.

### ✨ Features

- **Multiple Font Styles**: Support for various ASCII art fonts (standard, slant, big, etc.)
- **Rich Color Themes**: 14 built-in color themes including rainbow, ocean, fire, neon, and more
- **Gradient Directions**: Horizontal, vertical, and diagonal gradient effects
- **Rendering Modes**: Choose between outline and fill rendering styles
- **Animation Support**: Create animated ASCII art with customizable frame rates
- **File Output**: Save your creations to files
- **Easy CLI Interface**: Simple command-line interface for quick generation

### 🚀 Installation

#### Prerequisites
- Python 3.6 or higher
- pip package manager

#### Install from PyPI (Recommended)
```bash
pip install ascii-gradient-art
```

#### Install from source
```bash
git clone https://github.com/crazyZSShuo/ascii-gradient-art.git
cd ascii-gradient-art
pip install -e .
```

### 📖 Usage

#### Basic Usage
```bash
ascii-gradient-art --text "Hello World"
```

#### Advanced Examples

**Custom font and color theme:**
```bash
ascii-gradient-art --text "AWESOME" --font slant --color-theme fire
```

**Vertical gradient with fill mode:**
```bash
ascii-gradient-art --text "COOL" --gradient-direction vertical --render-mode fill
```

**Animated ASCII art:**
```bash
ascii-gradient-art --text "DANCE" --animation-frames 20 --animation-delay 0.1
```

**Save to file:**
```bash
ascii-gradient-art --text "SAVE ME" --output-file output.txt
```

#### Command Line Options

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `--text` | Text to convert to ASCII art | Required | - |
| `--font` | Font style for ASCII art | `standard` | Any pyfiglet font |
| `--color-theme` | Gradient color theme | `rainbow` | See [Color Themes](#color-themes) |
| `--gradient-direction` | Direction of the color gradient | `horizontal` | `horizontal`, `vertical`, `diagonal_up`, `diagonal_down` |
| `--render-mode` | Rendering mode | `outline` | `outline`, `fill` |
| `--animation-frames` | Number of animation frames | `1` | Any positive integer |
| `--animation-delay` | Delay between frames (seconds) | `0.1` | Any positive float |
| `--output-file` | Output file path | None | Any valid file path |

#### Color Themes

The tool includes 14 beautiful built-in color themes:

- **rainbow**: Classic rainbow colors (Red → Orange → Yellow → Green → Blue → Indigo → Violet)
- **ocean**: Ocean blues (Navy → Deep Sky Blue → Sky Blue)
- **fire**: Fire colors (Black → Dark Red → Orange Red → Dark Orange → Yellow)
- **forest**: Forest greens (Forest Green → Dark Olive Green → Olive Drab)
- **sunset**: Sunset colors (Orange → Orange Red → Dark Magenta)
- **pastel**: Soft pastel colors (Light Pink → Light Green → Light Blue → Light Yellow)
- **grayscale**: Black to white gradient
- **neon**: Bright neon colors (Cyan → Magenta → Yellow → Green)
- **candy**: Sweet candy colors (Pink → Light Blue → Yellow)
- **winter**: Winter theme (Navy → Light Blue → Snow)
- **autumn**: Autumn colors (Saddle Brown → Dark Orange → Gold)
- **spring**: Spring colors (Pale Green → Bisque → Pink)
- **vaporwave**: Retro vaporwave (Purple → Cyan → Hot Pink)
- **custom**: Customizable theme (Black → White by default)

### 🏗️ Project Structure

```
ascii_gradient_art/
├── ascii_gradient_art.py    # Main entry point
├── main.py                  # Alternative entry point
├── setup.py                 # Package configuration
├── core/
│   ├── __init__.py
│   ├── generator.py         # ASCII art generation and processing
│   └── color_utils.py       # Color manipulation utilities
├── themes/
│   ├── __init__.py
│   └── default_themes.py    # Built-in color themes
└── utils/
    ├── __init__.py
    └── cli_parser.py         # Command-line argument parsing
```

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

### 👤 Author

- **Maxzs**

---

## 中文

### 🎨 概述

ASCII 渐变艺术字是一个强大的命令行工具，可以生成带有自定义渐变色彩和动画效果的精美 ASCII 艺术字。将任何文本转换为令人惊叹的视觉艺术，支持多种字体、色彩主题和渲染模式。

### ✨ 功能特性

- **多种字体样式**: 支持各种 ASCII 艺术字体（standard、slant、big 等）
- **丰富的色彩主题**: 14 种内置色彩主题，包括彩虹、海洋、火焰、霓虹等
- **渐变方向**: 水平、垂直和对角线渐变效果
- **渲染模式**: 可选择轮廓或填充渲染样式
- **动画支持**: 创建可自定义帧率的动画 ASCII 艺术字
- **文件输出**: 将作品保存到文件
- **简易命令行界面**: 简单的命令行界面，快速生成艺术字

### 🚀 安装

#### 系统要求
- Python 3.6 或更高版本
- pip 包管理器

#### 从PyPI安装（推荐）
```bash
pip install ascii-gradient-art
```

#### 从源码安装
```bash
git clone https://github.com/crazyZSShuo/ascii-gradient-art.git
cd ascii-gradient-art
pip install -e .
```

### 📖 使用方法

#### 基本用法
```bash
ascii-gradient-art --text "Hello World"
```

#### 高级示例

**自定义字体和色彩主题:**
```bash
ascii-gradient-art --text "AWESOME" --font slant --color-theme fire
```

**垂直渐变与填充模式:**
```bash
ascii-gradient-art --text "COOL" --gradient-direction vertical --render-mode fill
```

**动画 ASCII 艺术字:**
```bash
ascii-gradient-art --text "DANCE" --animation-frames 20 --animation-delay 0.1
```

**保存到文件:**
```bash
ascii-gradient-art --text "SAVE ME" --output-file output.txt
```

#### 命令行选项

| 选项 | 描述 | 默认值 | 可选值 |
|------|------|--------|--------|
| `--text` | 要转换为 ASCII 艺术字的文本 | 必需 | - |
| `--font` | ASCII 艺术字的字体样式 | `standard` | 任何 pyfiglet 字体 |
| `--color-theme` | 渐变色彩主题 | `rainbow` | 参见 [色彩主题](#色彩主题) |
| `--gradient-direction` | 色彩渐变的方向 | `horizontal` | `horizontal`, `vertical`, `diagonal_up`, `diagonal_down` |
| `--render-mode` | 渲染模式 | `outline` | `outline`, `fill` |
| `--animation-frames` | 动画帧数 | `1` | 任何正整数 |
| `--animation-delay` | 帧间延迟（秒） | `0.1` | 任何正浮点数 |
| `--output-file` | 输出文件路径 | 无 | 任何有效文件路径 |

#### 色彩主题

工具包含 14 种精美的内置色彩主题：

- **rainbow**: 经典彩虹色（红 → 橙 → 黄 → 绿 → 蓝 → 靛 → 紫）
- **ocean**: 海洋蓝（海军蓝 → 深天蓝 → 天蓝）
- **fire**: 火焰色（黑 → 深红 → 橙红 → 深橙 → 黄）
- **forest**: 森林绿（森林绿 → 深橄榄绿 → 橄榄褐）
- **sunset**: 日落色（橙 → 橙红 → 深洋红）
- **pastel**: 柔和粉彩色（浅粉 → 浅绿 → 浅蓝 → 浅黄）
- **grayscale**: 黑白渐变
- **neon**: 明亮霓虹色（青 → 洋红 → 黄 → 绿）
- **candy**: 甜美糖果色（粉 → 浅蓝 → 黄）
- **winter**: 冬季主题（海军蓝 → 浅蓝 → 雪白）
- **autumn**: 秋季色彩（马鞍棕 → 深橙 → 金色）
- **spring**: 春季色彩（淡绿 → 淡黄褐 → 粉色）
- **vaporwave**: 复古蒸汽波（紫 → 青 → 热粉）
- **custom**: 可自定义主题（默认黑到白）

### 🏗️ 项目结构

```
ascii_gradient_art/
├── ascii_gradient_art.py    # 主入口点
├── main.py                  # 备用入口点
├── setup.py                 # 包配置
├── core/
│   ├── __init__.py
│   ├── generator.py         # ASCII 艺术字生成和处理
│   └── color_utils.py       # 色彩处理工具
├── themes/
│   ├── __init__.py
│   └── default_themes.py    # 内置色彩主题
└── utils/
    ├── __init__.py
    └── cli_parser.py         # 命令行参数解析
```

### 🤝 贡献

欢迎贡献！请随时提交 Pull Request。对于重大更改，请先开启 issue 讨论您想要更改的内容。

### 📄 许可证

本项目采用 MIT 许可证 - 详情请参见 LICENSE 文件。

### 👤 作者

- **Maxzs**

---

### 🎯 示例输出

以下是一些使用不同主题和设置的示例输出：

```bash
# 彩虹主题水平渐变
ascii-gradient-art --text "RAINBOW" --color-theme rainbow

# 火焰主题垂直渐变填充模式
ascii-gradient-art --text "FIRE" --color-theme fire --gradient-direction vertical --render-mode fill

# 霓虹主题对角渐变动画
ascii-gradient-art --text "NEON" --color-theme neon --gradient-direction diagonal_up --animation-frames 15
```

### 🔧 故障排除

**常见问题:**

1. **字体未找到错误**: 确保您使用的字体名称是 pyfiglet 支持的有效字体。
2. **色彩显示问题**: 确保您的终端支持 ANSI 色彩代码。
3. **动画播放问题**: 某些终端可能不完全支持清屏序列，这可能影响动画效果。

**获取可用字体列表:**
```python
import pyfiglet
print(pyfiglet.FigletFont.getFonts())
```

### 🌟 未来计划

- [ ] 添加更多内置色彩主题
- [ ] 支持自定义色彩主题配置文件
- [ ] 添加更多动画效果
- [ ] 支持图像到 ASCII 转换
- [ ] 添加 GUI 界面
- [ ] 支持更多输出格式（HTML、SVG 等）