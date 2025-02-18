# **Steganography Image Encryption & Decryption**

## **Overview**
This project implements an **image-based steganography system** that allows users to securely hide and retrieve secret messages within an image. The encryption algorithm converts plaintext into ciphertext by modifying pixel values, ensuring **confidentiality** and **data integrity**.

---
## **Features**
- **Secure Message Encryption**: Hides text messages inside image pixels.
- **Decryption with Passcode**: Only authorized users with the correct passcode can retrieve the message.
- **Cross-Platform Compatibility**: Works on **Windows, macOS, and Linux**.
- **Automatic Image Opening**: Opens the encrypted image based on the OS.

---
## **Technologies Used**
### **1. Hardware Requirements:**
- **Processor**: Multi-core processor (i5 or above recommended).
- **RAM**: Minimum 4GB (8GB recommended for larger encryption tasks).
- **Storage**: Minimal (10–20MB), sufficient disk space for encrypted images.
- **Network**: Required for downloading dependencies.

### **2. Software Requirements:**
- **Operating System**: Windows 10 or above, Linux, or macOS.
- **Programming Language**: Python 3.x.
- **Python Libraries**:
  - `OpenCV` (`cv2`): Handles image processing.
  - `OS`: Manages file operations.
  - `Platform`: Detects OS for executing system commands.
  - `String`: Handles character mapping and processing.

---
## **Installation & Setup**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/steganography.git
   cd steganography
   ```
2. **Create and Activate Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate  # Windows
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---
## **Usage**
### **Encryption**
1. Run the encryption script:
   ```bash
   python encrypt.py
   ```
2. Enter your secret message and passcode.
3. The encrypted image (`encryptedImage.jpg`) will be generated.

### **Decryption**
1. Run the decryption script:
   ```bash
   python decrypt.py
   ```
2. Enter the correct passcode to retrieve the hidden message.

---
## **End Users**
- **Cybersecurity Enthusiasts**: Learning encryption and steganography.
- **Journalists & Activists**: Secure communication in restricted environments.
- **Forensic & Intelligence Agencies**: Hiding and retrieving classified information.
- **Developers & Researchers**: Exploring encryption techniques in images.

---
## **Wow Factors**
- **End-to-End Encryption (E2EE)**: Ensures data security during transmission.
- **Real-Time Secure Messaging**: Encrypts messages in real-time with integrity checks.
- **Quantum-Resistant Encryption**: Future-proof security against quantum computing threats.
- **Zero-Knowledge Proof Authentication**: Verifies identity without revealing sensitive data.

---
## **Future Scope**
- **Support for More Image Formats**: Expand beyond JPG/PNG to other formats.
- **Integration with Cloud Storage**: Securely store encrypted images online.
- **Mobile Application**: Develop an Android/iOS app for easy encryption on mobile devices.

---
## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## **Contributing**
We welcome contributions! Feel free to fork the repo, make changes, and submit a pull request.
 

