# HashHaven 

## Introduction
This Python script generates hash grabbing files for Windows systems to capture hashes from victim machines. It creates shortcut files (.scf and .lnk) that, when opened by a user, initiate hash capturing mechanisms.

## Table of Contents
  1. Requirements
  2. Installation
  3. Usuage
  4. Instructions
  5. Disclaimer

## Requirements

- Python 3
- `pylnk3` library for creating shortcut files (`lnk`)
- Windows operating system (for `.lnk` file execution)

## Installation
  1. Clone the repository or download the `HashHaven.py` file.

  
<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/1f554bff-b0b6-412f-b39b-4f3c985f6c76" alt="Step 3">
  </div>
  
  2. use the command in your linux machine git clone https://github.com/FaisalJaman1012/HashHaven.git

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/85771ea2-6b34-467f-92d3-5dd32b6ecffd" alt="Step 3">
  </div>
  
  3. Install the requirements by running the command sudo pip install -r requirements.txt

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/8980e09a-9807-467a-b81c-8c80d8649e52" alt="Step 3">
  </div>

## Usage

  1. Run the script using Python3. run python3 HashHaven.py

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/6e6c13d3-c7ac-4739-bb4c-2f1ea819f29d" alt="Step 3">
  </div>

  2. Follow the prompts to enter the attacker's IP address and the desired output name.

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/a72058c7-eb4f-4207-8cf3-3c357b5dcbd8" alt="Step 3">
  </div>

  3. The script will generate hash grabbing files: `.scf` and `.lnk`.

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/cc0871c4-f198-41e8-96d0-f5c42dd7b076" alt="Step 3">
  <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/4e16fc34-8fad-40cd-b6b3-8142578c9782" alt="Step 3">
  </div>

  4. Upload these files to an SMB share and capture hashes using tools like  `smbserver.py/responder`.

<div style="text-align:center">
    <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/dc11e0f4-4f6d-4e28-b199-cdfe6502bd60" alt="Step 3">
  <img src="https://github.com/FaisalJaman1012/HashHaven/assets/91938237/3d98414f-4c85-4a35-b220-c6b2e31c2939" alt="Step 3">
  </div>


## Instructions

- **IP Address:** Enter the IP address of the attacker machine. This is where captured hashes will be sent.
- **Output Name:** Choose a name for the output files. This will be used as the base name for generated files.

## Disclaimer

This script is intended for educational and testing purposes only. Misuse of this script for unauthorized access or any malicious activity is illegal and unethical. Use it responsibly and only on systems you are authorized to test.








