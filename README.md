```
   _______    ____     __               __               
  /  _/ _ \\  / __/_ __/ /________ _____/ /____  ____ 
 _/ // ___/ / _/ \\ \\ / __/ __/ _ `/ __/ __/ _ \\/ __/
/___/_/    /___//_\\_\\\\__/_/  \\_,_/\\__/\\__/\\___/_/
```
# Export IP addresses from PDF to TXT, CSV and JSON files

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-3.3.1-brightgreen)

**IP Extractor** is a command-line tool designed to extract unique IP addresses from PDF documents. This open-source, Python-based tool is ideal for professionals in security operations centers (SOCs), open-source intelligence (OSINT), and DevOps who need to analyze documents, logs, or reports for network-related information. The tool parses PDF files, identifies valid public IP addresses, and exports them to TXT, CSV, and JSON files for further analysis.

## 📑 Table of Contents
- [Features](#features)
- [Target Audience](#target-audience)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Example Output](#example-output)
- [Demo](#demo)
- [Screenshots](#screenshots)
- [Development Environment](#development-environment)
- [Music That Fueled Development](#music-that-fueled-development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🚀 Features
- **Extracts Public IPs**: Identifies and extracts only valid, public IP addresses (excludes private ranges like 10.0.0.0/8).
- **PDF Processing**: Uses `PyPDF2` to parse text from PDF documents.
- **User-Friendly CLI**: Intuitive command-line interface with colorful output powered by the `rich` library.
- **Automatic Dependency Installation**: Automatically installs missing Python packages (`PyPDF2`, `rich`).
- **Progress Tracking**: Displays a progress bar while processing PDF pages.
- **Sorted Output**: Saves extracted IPs in a sorted text file for easy analysis.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🎯 Target Audience
This tool is designed for:
- **SOC Analysts**: To extract IPs from incident reports or threat intelligence PDFs.
- **OSINT Researchers**: To analyze documents for network-related information.
- **DevOps Engineers**: To process log files or configuration documents in PDF format.
- **Cybersecurity Enthusiasts**: For learning and experimenting with IP extraction workflows.

---

## 💾 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lukaszwojcikdev/ip-extractor.git
   cd ip-extractor
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   The tool automatically installs required packages (`PyPDF2`, `rich`) on first run. Alternatively, you can install them manually:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tool**:
   ```bash
   python ip_extractor.py --help
   ```

---

## 📦 Dependencies
The tool relies on the following Python libraries:
- **PyPDF2**: For reading and extracting text from PDF files.
- **rich**: For enhanced terminal output with colors and progress bars.
- **ipaddress**: Built-in library for validating IP addresses.
- **argparse**: Built-in library for parsing command-line arguments.
- **subprocess**: Built-in library for automatic package installation.

Install manually with:
```bash
pip install PyPDF2 rich
```

---

## 🧑‍💻 Usage
Run the tool using the following command structure:
```bash
python ip_extractor.py [options]
```

### ⚙️ Available Options
| Option              | Description                                    |
|---------------------|------------------------------------------------|
| `-e, --extract FILE`| Extract IPs from the specified PDF file        |
| `-c, --csv`         | Export results to a CSV file                   |
| `-j, --json`        | Export results to a JSON file                  |
| `-i, --info`        | Display program and author information         |
| `-v, --version`     | Show the tool's version                        |
| `-h, --help`        | Display the help screen                        |

### 📝 Example Commands
- Extract IPs from a PDF:
  ```bash
  python ip_extractor.py -e document.pdf
  ```
- Export to a CSV file:
  ```bash
  python ip_extractor.py -c
  ```
- Export to a JSON file:
  ```bash
  python ip_extractor.py -j
  ```
- Show version:
  ```bash
  python ip_extractor.py -v
  ```
- Display help:
  ```bash
  python ip_extractor.py -h
  ```

---

## Example Output
When you run:
```bash
python ip_extractor.py -e sample.pdf
```

The tool processes `sample.pdf`, extracts public IP addresses, and saves them to `sample_ips.txt`. Example output in the terminal:
```
   _______    ____     __               __
  /  _/ _ \  / __/_ __/ /________ _____/ /____  ____
 _/ // ___/ / _/ \ \ / __/ __/ _ `/ __/ __/ _ \/ __/
/___/_/    /___//_\\_\\__/_/  \_,_/\\__/\\__/\\___/_/
⚡ "Because every PDF has something to hide."

🔄 Przetwarzanie  : sample.pdf
📄 Przeszukiwanie stron: [████████████████████] 100%
🌐 Znaleziono     : 5 unikalnych adresów IP!
💾 Zapisano do    : sample_ips.txt
```

The `sample_ips.txt` file might contain:
```
104.16.249.5
172.217.16.78
198.51.100.23
203.0.113.10
```

---

## 🎬 Demo
A short demo video showcasing the tool's functionality is available [here](https://lukk.eu/ip-extractor-demo.mp4). It demonstrates:
1. Running the tool with a sample PDF.
2. Displaying the help and info screens.
3. Viewing the output file with extracted IPs.

---

## 🖼️ Screenshots
### Help Screen
![Help Screen](screenshots/help_screen.png)

### 🔍 Extraction Process
![Extraction Process](screenshots/extraction_process.png)

### 📁 Output File
![Output File](screenshots/output_file.png)

*Note: Screenshots are placeholders. Actual screenshots can be found in the `screenshots/` directory of the repository.*

---

## 🛠️ Development Environment
The tool was developed using:
- **IDE**: Notepad++
- **Testing Environment**: Python 3.12+ on Windows 11
- **Package Management**: `pip` with virtual environments
- **Documentation**: Markdown for README and comments within the code

---

## 🎶 Music That Fueled Development
The coding sessions were powered by:
- **CYBERNOCTURE** -  [Synthwave & Electroclash with Future Bass Mix for Late-Nigh Coding](https://www.youtube.com/watch?v=xm12zz95lb8&list=PLeSTc7e2DKcrUo5xzCJ_udrmdmoe6g8RO)

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 🧭 Comming Soon
* Added unit tests: A separate test_ip_extractor.py file with tests for validation, extraction, and export functions.
* IPv6 support: Extracts not only IPv4 addresses, but also IPv6 addresses (ipaddress.IPv6Address).
* WHOIS integration: Checks IP owner information, registration dates, DNS servers, etc.
* Automatic IP extraction from all PDF files in a folder.
* Exports TXT, CSV, and JSON using a single --all flag.
* Error handling with logging: log.txt with a full error traceback of the session errors.
* Ensuring correct file saving on systems with various encodings (UTF-8, cp1250, etc.).


---

## ⚠️ Disclaimer
By using this software, you agree to these terms. The software is provided as-is, and you use it at your own risk. The author does not accept any responsibility for damages or issues caused by the use of this software.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact
For questions or feedback:
- **GitHub**: [https://github.com/lukaszwojcikdev/ip-extractor.git](https://github.com/lukaszwojcikdev/ip-extractor.git)
- **LinkedIn**: [https://linkedin.com/h/lukasz-michal-wojcik](https://linkedin.com/h/lukasz-michal-wojcik)
- **Dev.to**: [https://dev.to/lukaszwojcikdev](https://dev.to/lukaszwojcikdev)
- **Website**: [https://lukaszwojcik.eu](https://lukaszwojcik.eu)
