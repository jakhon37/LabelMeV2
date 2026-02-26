"""Dark mode stylesheet and utilities for labelme."""

from __future__ import annotations

DARK_STYLESHEET = """
/* Main Application */
QWidget {
    background-color: #2b2b2b;
    color: #d4d4d4;
    font-size: 13px;
}

/* Main Window */
QMainWindow {
    background-color: #1e1e1e;
}

/* Menu Bar */
QMenuBar {
    background-color: #2d2d2d;
    color: #cccccc;
    border-bottom: 1px solid #3e3e3e;
}

QMenuBar::item {
    background-color: transparent;
    padding: 4px 12px;
}

QMenuBar::item:selected {
    background-color: #094771;
}

QMenuBar::item:pressed {
    background-color: #0e639c;
}

/* Menu */
QMenu {
    background-color: #252526;
    color: #cccccc;
    border: 1px solid #454545;
}

QMenu::item {
    padding: 5px 25px 5px 20px;
}

QMenu::item:selected {
    background-color: #094771;
}

QMenu::separator {
    height: 1px;
    background: #3e3e3e;
    margin: 5px 0px;
}

/* Tool Bar */
QToolBar {
    background-color: #2d2d2d;
    border: 1px solid #3e3e3e;
    spacing: 3px;
    padding: 3px;
}

QToolBar::separator {
    background-color: #3e3e3e;
    width: 1px;
    margin: 3px;
}

QToolButton {
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 3px;
    padding: 3px;
    margin: 2px;
}

QToolButton:hover {
    background-color: #3e3e3e;
    border: 1px solid #094771;
}

QToolButton:pressed {
    background-color: #094771;
}

QToolButton:checked {
    background-color: #0e639c;
    border: 1px solid #007acc;
}

/* Status Bar */
QStatusBar {
    background-color: #007acc;
    color: #ffffff;
    border-top: 1px solid #007acc;
}

QStatusBar QLabel {
    background-color: transparent;
    color: #ffffff;
    padding: 2px 5px;
}

/* Dock Widgets */
QDockWidget {
    color: #cccccc;
    titlebar-close-icon: url(close.png);
    titlebar-normal-icon: url(float.png);
}

QDockWidget::title {
    background-color: #2d2d2d;
    text-align: left;
    padding: 6px;
    border: 1px solid #3e3e3e;
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    background: transparent;
    padding: 0px;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: #3e3e3e;
}

/* List Widgets */
QListWidget {
    background-color: #252526;
    color: #cccccc;
    border: 1px solid #3e3e3e;
    outline: none;
}

QListWidget::item {
    padding: 4px;
    border: none;
}

QListWidget::item:selected {
    background-color: #094771;
    color: #ffffff;
}

QListWidget::item:hover {
    background-color: #2a2d2e;
}

QListWidget::item:selected:hover {
    background-color: #0e639c;
}

/* Scroll Bars */
QScrollBar:vertical {
    background-color: #1e1e1e;
    width: 14px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #424242;
    min-height: 20px;
    border-radius: 2px;
}

QScrollBar::handle:vertical:hover {
    background-color: #4e4e4e;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #1e1e1e;
    height: 14px;
    margin: 0px;
}

QScrollBar::handle:horizontal {
    background-color: #424242;
    min-width: 20px;
    border-radius: 2px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4e4e4e;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Line Edit */
QLineEdit {
    background-color: #3c3c3c;
    color: #cccccc;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
    padding: 4px;
    selection-background-color: #094771;
}

QLineEdit:focus {
    border: 1px solid #007acc;
}

/* Push Buttons */
QPushButton {
    background-color: #0e639c;
    color: #ffffff;
    border: 1px solid #0e639c;
    border-radius: 2px;
    padding: 5px 15px;
    min-width: 60px;
}

QPushButton:hover {
    background-color: #1177bb;
    border: 1px solid #1177bb;
}

QPushButton:pressed {
    background-color: #094771;
    border: 1px solid #094771;
}

QPushButton:disabled {
    background-color: #3e3e3e;
    color: #6e6e6e;
    border: 1px solid #3e3e3e;
}

/* Combo Box */
QComboBox {
    background-color: #3c3c3c;
    color: #cccccc;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
    padding: 4px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #007acc;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox::down-arrow {
    image: url(down_arrow.png);
}

QComboBox QAbstractItemView {
    background-color: #252526;
    color: #cccccc;
    border: 1px solid #454545;
    selection-background-color: #094771;
    outline: none;
}

/* Spin Box */
QSpinBox, QDoubleSpinBox {
    background-color: #3c3c3c;
    color: #cccccc;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
    padding: 4px;
}

QSpinBox:focus, QDoubleSpinBox:focus {
    border: 1px solid #007acc;
}

/* Check Box */
QCheckBox {
    color: #cccccc;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    background-color: #3c3c3c;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
}

QCheckBox::indicator:hover {
    border: 1px solid #007acc;
}

QCheckBox::indicator:checked {
    background-color: #007acc;
    border: 1px solid #007acc;
}

/* Radio Button */
QRadioButton {
    color: #cccccc;
    spacing: 5px;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
    background-color: #3c3c3c;
    border: 1px solid #3e3e3e;
    border-radius: 8px;
}

QRadioButton::indicator:hover {
    border: 1px solid #007acc;
}

QRadioButton::indicator:checked {
    background-color: #007acc;
    border: 1px solid #007acc;
}

/* Slider */
QSlider::groove:horizontal {
    background-color: #3c3c3c;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #007acc;
    width: 14px;
    height: 14px;
    margin: -4px 0;
    border-radius: 7px;
}

QSlider::handle:horizontal:hover {
    background-color: #1177bb;
}

/* Progress Bar */
QProgressBar {
    background-color: #3c3c3c;
    color: #cccccc;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #007acc;
    border-radius: 2px;
}

/* Tab Widget */
QTabWidget::pane {
    background-color: #2b2b2b;
    border: 1px solid #3e3e3e;
}

QTabBar::tab {
    background-color: #2d2d2d;
    color: #cccccc;
    padding: 6px 12px;
    border: 1px solid #3e3e3e;
    border-bottom: none;
}

QTabBar::tab:selected {
    background-color: #2b2b2b;
    border-bottom: 2px solid #007acc;
}

QTabBar::tab:hover {
    background-color: #3e3e3e;
}

/* Group Box */
QGroupBox {
    color: #cccccc;
    border: 1px solid #3e3e3e;
    border-radius: 2px;
    margin-top: 10px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    color: #007acc;
}

/* Dialog */
QDialog {
    background-color: #2b2b2b;
}

QDialog QPushButton {
    min-width: 80px;
}

/* Message Box */
QMessageBox {
    background-color: #2b2b2b;
}

QMessageBox QLabel {
    color: #cccccc;
}

/* Tool Tip */
QToolTip {
    background-color: #252526;
    color: #cccccc;
    border: 1px solid #454545;
    padding: 4px;
}

/* Scroll Area */
QScrollArea {
    background-color: #1e1e1e;
    border: none;
}

/* Label */
QLabel {
    background-color: transparent;
    color: #d4d4d4;
}

/* Splitter */
QSplitter::handle {
    background-color: #3e3e3e;
}

QSplitter::handle:hover {
    background-color: #007acc;
}
"""


def get_dark_stylesheet() -> str:
    """Get the dark mode stylesheet.

    Returns:
        The complete dark mode stylesheet as a string.
    """
    return DARK_STYLESHEET
