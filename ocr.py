import sys
import easyocr
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.Qt import QClipboard
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
import numpy as np

class ClipboardWatcher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reader = easyocr.Reader(['en'])
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.on_clipboard_change)

    def initUI(self):
        self.setWindowTitle('OCR Clipboard Monitor')
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.textArea = QTextEdit()
        self.textArea.setReadOnly(True)
        self.layout.addWidget(self.textArea)
        self.setLayout(self.layout)

    def on_clipboard_change(self):
        mime = self.clipboard.mimeData()
        if mime.hasImage():
            self.textArea.clear()
            qimage = self.clipboard.image()
            if not qimage.isNull():
                # Convert QImage to numpy array
                qimage = QImage(qimage).convertToFormat(QImage.Format.Format_RGB32)
                width = qimage.width()
                height = qimage.height()

                ptr = qimage.bits()
                ptr.setsize(height * width * 4)
                arr = np.array(ptr).reshape(height, width, 4)  # 4 for RGBA

                # Convert numpy array to PIL Image
                pil_img = Image.fromarray(arr[..., :3])  # Discard the alpha channel
                text = self.extract_text(pil_img)
                self.textArea.setText(text)

    def extract_text(self, image):
        result = self.reader.readtext(np.array(image))
        extracted_text = '\n'.join([detection[1] for detection in result])
        return extracted_text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClipboardWatcher()
    ex.show()
    sys.exit(app.exec_())
