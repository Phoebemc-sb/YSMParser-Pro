import sys
import os
import subprocess
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget, QFileDialog, QTextEdit, QLabel, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

class YSMGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YSM Parser Pro - 极客版")
        self.resize(700, 500)
        
        # --- 全局样式表 (QSS) ---
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QLabel {
                color: #dcdcdc;
                font-family: "Microsoft YaHei";
                font-size: 14px;
            }
            QTextEdit {
                background-color: #2d2d2d;
                color: #569cd6;
                border: 1px solid #3f3f46;
                border-radius: 8px;
                font-family: "Consolas";
                font-size: 12px;
                padding: 10px;
            }
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 6px;
                font-weight: bold;
                font-size: 15px;
                min-height: 45px;
            }
            QPushButton:hover {
                background-color: #1c97ea;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """)

        # 主布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # 标题区域
        self.title_label = QLabel("YSM 资源批量解密工具")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff;")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # 提示横线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #3f3f46;")
        layout.addWidget(line)

        self.info_label = QLabel("请确保 YSMParser.exe 与本工具放置在同一目录下")
        layout.addWidget(self.info_label)

        # 核心按钮
        self.btn = QPushButton("📂 选择模型文件夹并解析")
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.start_parse)
        layout.addWidget(self.btn)

        # 日志区域
        self.log_area = QTextEdit()
        self.log_area.setPlaceholderText("等待任务启动...")
        layout.addWidget(self.log_area)

        self.setCentralWidget(central_widget)

    def start_parse(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择包含 .ysm 文件的文件夹")
        
        if dir_path:
            dir_path = dir_path.replace('/', os.sep)
            self.log_area.clear()
            self.log_area.append(f"<b>[ 任务启动 ]</b> 目标目录: {dir_path}\n")
            
            try:
                output_dir = os.path.join(os.getcwd(), "output")
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                command = ["YSMParser.exe", "--input", dir_path, "--output", output_dir]
                
                # 运行解析
                result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
                
                if result.stdout:
                    self.log_area.append(result.stdout)
                if result.stderr:
                    self.log_area.append(f"<span style='color:#ce9178;'>提示: {result.stderr}</span>")
                
                self.log_area.append(f"\n<b style='color:#4ec9b0;'>[ 任务成功 ]</b> 解析已完成，结果保存在 output 文件夹。")
                
            except Exception as e:
                self.log_area.append(f"<b style='color:#f44747;'>[ 运行失败 ]</b>: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YSMGui()
    window.show()
    sys.exit(app.exec())