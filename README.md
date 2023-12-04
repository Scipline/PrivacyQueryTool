# Privacy Query Software 🔎

This is a simple privacy query software built with PySide6. It can query related information of QQ numbers, mobile phone numbers, and Weibo IDs.

## Disclaimer ⚠️

- This software calls public APIs to query information. Please do not use it for illegal activities.
- It's for querying your own privacy leakage situation. The code is for communication and learning only. The user assumes all consequences, the author is not responsible. By downloading the source code, you agree to this agreement.

## Features 🛠️

1. **QQ Binding Query**: Enter a QQ number, click on query, and you can obtain related information of this QQ number.
2. **Mobile Number Reverse Query**: Enter a mobile number, click on query, and you can obtain related information of this mobile number.
3. **Weibo Binding Query**: Enter a Weibo ID, click on query, and you can obtain related information of this Weibo ID.

## Installation 💻

Ensure that you have Python 3.8 or a higher version installed on your computer.

First, you need to install the project dependencies. In the root directory of the project, run the following command:

If you have PDM installed:

```bash
pdm sync
```

If you don't have PDM installed, but you have pip, you can use the following command:

```bash
pip install -r requirements.txt
```

This will install the following dependencies:

- PySide6
- requests
- pyperclip

## Running the Software 🚀

In the root directory of the project, run the following command:

```bash
cd src
python main.py
```

Then, you can query in the pop-up window.

## Note ⚠️

This software is for learning and research purposes only and should not be used for any illegal purposes. All consequences arising from the use of this software are to be borne by the user.

## License 📄

MIT
