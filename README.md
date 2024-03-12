# Table of Contents

[Overview](#overview)
[Usage](#usage)
[Requirements](#requirements)
[License](#license)
[Contribution](#contribution)
[Future plans](#future-plans)
[Authors](#authors)

# Overview

This Python project implements a symmetric encryption algorithm for secure password management, designed for learning purposes. It allows users to store sensitive information, such as usernames and passwords, in an encrypted format within a file. The encryption ensures the confidentiality of the stored data, providing an added layer of security.
This project is intended for educational purposes only. The code is provided as-is, without any guarantee or warranty. Use at your own risk.

### Symmetric Encryption

This encryption method uses a symmetric key, meaning the same password is used for both encryption and decryption. Users must remember their chosen password to access and manage their stored credentials.

### Password Generator

Included in the project is a helpful Bash script for generating secure passwords of any length. Users can leverage this feature to create strong, unique passwords for their accounts.

### Secure Credential Retrieval

To retrieve stored account information, users must provide the correct encryption key and specify the domain name associated with the desired credentials. This ensures that only authorized users can access and view their sensitive data.

# Usage

## Encrypting Account Information

To add a new account to the encrypted file, run the symmetric_encrypt.sh script with the following command:

    `./symmetric_encrypt.sh <file_path> <domain_name> <username> <password>`

You will be prompted to enter a key, and the encrypted account information will be stored in the specified file.

## Decrypting Account Information

To retrieve account information from the encrypted file, run the symmetric_decrypt.sh script with the following command:

    `./symmetric_decrypt.sh <file_path> <domain_name>`

Enter the key used for encryption, and the decrypted username and password will be displayed.

## Password Generation

To generate a secure password, run the provided Bash script:

    `./password_generator.sh`

# Requirements

- [Python 3.x](https://www.python.org/downloads/)

# License

This project is licensed under the [MIT License](https://opensource.org/license/mit), allowing for flexible use and modification.

# Contribution

Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.
If you'd like to contribute to the project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature: git checkout -b feature-name.
- Make your changes and commit: git commit -m 'Add some feature'.
- Push to your fork: git push origin feature-name.
- Open a pull request.

# Future plans

In the upcoming stages of development, the project aims to achieve the following:

1. **Code Testing:**
   - Thoroughly test the entire codebase to ensure its reliability and identify any potential issues or bugs.

2. **Implementing Asymmetric Encryption:**
   - Develop and integrate an asymmetric encryption algorithm to enhance the project's capabilities. This addition will focus on encrypting and decrypting messages and data, expanding the application beyond password management.

# Authors

List of the contributors to the project:

<a href="https://github.com/SebestyenBenedek/encryption/graphs/contributors">
 <img src="https://contrib.rocks/image?repo=SebestyenBenedek/encryption" />
</a>