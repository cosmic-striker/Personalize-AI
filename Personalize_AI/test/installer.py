import subprocess
def run_pip_command(package_name):
    try:
        subprocess.run(['pip', 'install', package_name], check=True)
        print(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")

package_to_install = [
    "SpeechRecognition",
    "pyttsx3",
    "wikipedia-api",
    "speedtest-cli",
    "pyjokes",
    "emoji",
    "pywhatkit"
]
for install in package_to_install:

    run_pip_command(install)
    print(install,"installed successfuly")