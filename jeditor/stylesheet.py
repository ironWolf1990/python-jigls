STYLE_QMENUBAR = """
QMenuBar {
    background-color: rgb(49,49,49);
    color: rgb(255,255,255);
    border: 1px solid #000;
}

QMenuBar::item {
    background-color: rgb(49,49,49);
    color: rgb(255,255,255);
}

QMenu {
    background-color: rgb(49,49,49);
    color: rgb(255,255,255);
    border: 1px solid #000;           
}

QMenu::item {
    padding: 5px 18px 2px;
    background-color: transparent;
}
QMenu::item:selected {
    color: rgba(98, 68, 10, 255);
    background-color: rgba(219, 158, 0, 255);
}
QMenu::separator {
    height: 1px;
    background: rgba(255, 255, 255, 50);
    margin: 4px 8px;
}
"""

STYLE_SPLASH = """
QFrame {
    background-color: #2F4454;
}
"""