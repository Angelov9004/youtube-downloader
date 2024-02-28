import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget, QFileDialog
from PyQt6.QtGui import QPixmap
from pytube import YouTube

class VideoDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Downloader")
        self.resize(500, 700)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Set background color
        self.setStyleSheet("background-color: #f0f0f0;")

        # Add logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png")
        pixmap = pixmap.scaled(450, 450)  # Resize pixmap to 450x450 pixels
        logo_label.setPixmap(pixmap)
        layout.addWidget(logo_label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube video URL")
        layout.addWidget(self.url_input)
        layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetFixedSize)
        layout.addStretch()

        download_button = QPushButton("Download")
        download_button.clicked.connect(self.downloadVideo)
        layout.addWidget(download_button)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)

        # Add author label as a hyperlink
        author_label = QLabel()
        author_label.setText('<a href="https://github.com/angelov9004">Developed by Angelov</a>')
        author_label.setOpenExternalLinks(True)  # Open link in external browser
        layout.addWidget(author_label)

    def downloadVideo(self):
        url = self.url_input.text()
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()

            # Open a file dialog for the user to choose the download location
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.FileMode.Directory)
            download_folder = file_dialog.getExistingDirectory(self, "Select Download Folder")

            if download_folder:
                stream.download(output_path=download_folder)
                self.status_label.setText("Download completed successfully.")
            else:
                self.status_label.setText("Download canceled.")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = VideoDownloader()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
