OCR Clipboard Monitor
=====================

A simple PyQt5 application that uses the EasyOCR library to monitor the clipboard for images and extract any text found in them.

Requirements
------------

* Python 3.x
* PyQt5
* EasyOCR
* numpy
* pillow (Python Imaging Library)

Installation
------------

1. Clone the repository or download the script.
2. Install the required packages using pip:
```
pip install PyQt5 EasyOCR numpy numpy pillow
```

Usage
-----

1. Run the script using Python:
```
python ocr_clipboard_monitor.py
```
2. The application will open and start monitoring the clipboard.
3. Copy an image containing text to the clipboard.
4. The application will automatically extract the text from the image and display it in the text area.

Use Cases
----------

* Quickly extracting text from images, such as screenshots or scanned documents, without having to manually type it out.
* Automating the process of extracting data from images for use in other applications or datasets.
* Accessibility for individuals who have difficulty reading small or stylized text in images.

Note
----

* The current implementation only supports English language OCR.
* The accuracy of the OCR will depend on the quality and clarity of the text in the image.

License
-------

This project is licensed under the MIT License - see the LICENSE.md file for details.
