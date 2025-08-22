# 精致贪吃蛇 (Snake Game)

一个使用 `pywebview` 和 HTML/CSS/JavaScript 构建的简易桌面贪吃蛇(snake)游戏。
![snake.jpg](https://fastly.jsdelivr.net/gh/ylicen/pictures@main/2025-08/snake_1755844067656.jpg)

## 项目介绍

使用前端技术,选择 `pywebview` 是为了规避 Electron 和 Tauri 等框架的复杂性，实现无需复杂配置即可运行的桌面应用。游戏逻辑和界面完全由 Web 技术（HTML, CSS, JavaScript）实现，通过 `pywebview` 将其包装为桌面应用。

## 技术栈

- **后端/桌面应用框架**: [pywebview](https://pywebview.flowrl.com/) - 用于创建桌面窗口并加载本地 HTML 文件。
- **前端框架**: 原生 HTML, CSS (Tailwind CSS), JavaScript。
- **样式**: [Tailwind CSS](https://tailwindcss.com/) - 用于快速构建自定义设计。
- **音效**: [Tone.js](https://tonejs.github.io/) - 用于在游戏中播放音效。
- **打包工具**: [PyInstaller](https://pyinstaller.org/) - 用于将 Python 应用及其资源打包成独立的可执行文件。
- **构建工具**: [Node.js](https://nodejs.org/) 和 [npm](https://www.npmjs.com/) - 用于构建 Tailwind CSS。



## 安装和运行

### 开发环境运行

1.  **安装 Python 依赖**:
    确保已安装 Python 3.x，然后安装 `pywebview`。
    ```bash
    pip install pywebview
    ```

2.  **安装 Node.js 依赖**:
    确保已安装 Node.js 和 npm，然后安装项目依赖。
    ```bash
    npm install
    ```

3.  **构建 CSS**:
    使用 Tailwind CSS 构建生产环境的 CSS 文件。
    ```bash
    npm run build:css
    ```

4.  **运行应用**:
    ```bash
    python app.py
    ```

## 打包和分发

一键打包:pyinstaller --noconfirm --log-level=WARN --onefile --windowed --icon="logo.ico" --add-data "index.html;." --add-data "tailwind.css;." --add-data "node_modules/tone/build/Tone.js;node_modules/tone/build" --name="snakeGame" app.py