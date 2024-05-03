# HashHaven 

This Python script generates hash grabbing files for Windows systems to capture hashes from victim machines. It creates shortcut files (.scf and .lnk) that, when opened by a user, initiate hash capturing mechanisms.

## Table of Contents
  1. Intoduction
  2. Requirements
  3. Installation
  4. Usuage
  5. Disclaimer

## Introduction

## Requirements

- Python 3
- `pylnk3` library for creating shortcut files (`lnk`)
- Windows operating system (for `.lnk` file execution)

## Installation
  1. Clone the repository or download the `HashHaven.py` file.
     <div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/1f554bff-b0b6-412f-b39b-4f3c985f6c76" alt="Step 3">
  </div>
  
  2.     

## Usage

1. 
2. Run the script using Python 3.
3. Follow the prompts to enter the attacker's IP address and the desired output name.
4. The script will generate hash grabbing files: `.scf` and `.lnk`.
5. Upload these files to an SMB share and capture hashes using tools like  `smbserver.py/responder`.


## Instructions

- **IP Address:** Enter the IP address of the attacker machine. This is where captured hashes will be sent.
- **Output Name:** Choose a name for the output files. This will be used as the base name for generated files.

## Disclaimer

This script is intended for educational and testing purposes only. Misuse of this script for unauthorized access or any malicious activity is illegal and unethical. Use it responsibly and only on systems you are authorized to test.

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/85771ea2-6b34-467f-92d3-5dd32b6ecffd" alt="Step 3">
  </div>




