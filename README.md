# 🫂File Hash Generator

A lightweight and efficient Python tool to generate cryptographic hash values for files. This utility helps verify file integrity, detect tampering, and perform basic security analysis using industry-standard hashing algorithms.

---

📌 Overview

File Hash Generator computes multiple hash digests of a file simultaneously, making it useful for:

- Integrity verification
- Malware analysis
- Digital forensics
- Secure file comparison

It currently supports:

- MD5
- SHA1
- SHA256

---

🚀 Features

- Fast chunk-based file reading (memory efficient)
- Multiple hash algorithms in one run
- Clean modular code structure
- Beginner-friendly yet scalable architecture
- CLI-based execution

---

📂 Project Structure

file-hash-generator/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── core/
│   └── hasher.py
│
├── utils/
│   └── file_handler.py
│
└── tests/
    └── test_hash.py

---

⚙️ Installation

Clone repository:

git clone https://github.com/Hero24-x/File-Hash-Generator/tree/main
cd file-hash-generator

No external dependencies required.

---

▶️ Usage

Run the script with file path:

python main.py example.txt

Example Output:

Hash Results:

MD5: e2fc714c4727ee9395f324cd2e7f331f
SHA1: a9993e364706816aba3e25717850c26c9cd0d89d
SHA256: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

---

🧪 Running Tests

pytest tests/

---

🛡️ Use Cases

- Verify downloaded files
- Compare original vs modified files
- Malware sample validation
- Evidence verification in investigations

---

🔮 Future Improvements

Planned enhancements:

- Folder hashing
- Drag-and-drop GUI
- Hash comparison mode
- VirusTotal API integration
- Multithreaded hashing

---

🤝 Contributing

Contributions are welcome. To contribute:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Submit pull request

---

📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.

---

⭐ Support

If you find this project useful, consider giving it a star. It helps others discover it and motivates further development.
