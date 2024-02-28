# youtube
Youtube Video downloader

 To convert your Python script (*.py) to an executable (*.exe), you can use various tools available. One commonly used tool is PyInstaller, which is compatible with PyQt applications. Here's how you can use PyInstaller to create an executable from your Python script:

 Install PyInstaller: If you haven't already installed PyInstaller, you can install it via pip:

pip install pyinstaller

Navigate to your script directory: Open a terminal or command prompt and navigate to the directory containing your Python script (Youtube_Downloader.py in this case).

Run PyInstaller: Run PyInstaller with the following command:
pyinstaller --onefile VideoDownloader.py



--onefile option bundles everything into a single executable file. You can omit this option if you prefer to have multiple files.
VideoDownloader.py should be replaced with the name of your Python script.
Locate the executable: After PyInstaller finishes, you can find the generated executable in the dist directory within your script's directory.

Run the executable: You can run the generated executable (VideoDownloader.exe) by double-clicking it or executing it from the command line.

PyInstaller will analyze your script, gather all necessary dependencies (including PyQt6 and pytube), and package them into a standalone executable. It's worth noting that the size of the resulting executable may be larger than the original script due to including all dependencies.

Additionally, depending on your operating system and requirements, you might need to make adjustments to the PyInstaller command or include additional options. For example, on Windows, you may need to specify --windowed option if you don't want a console window to appear when running the executable.
