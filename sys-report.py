#!/usr/bin/python3

import sys, os, shutil, subprocess


def installed(command):
    return shutil.which(command) is not None


def prompt_install(command):
    print(f"The command '{command}' is not installed. Please install it and try again.")
    sys.exit(1)


def run_command(command):
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{' '.join(command)}': {e.stderr}")
        sys.exit(1)


def upload_to_termbin(data):
    try:
        process = subprocess.Popen(
            ["nc", "termbin.com", "9999"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        url, _ = process.communicate(input=data)
        if process.returncode == 0:
            return url.strip()
        else:
            print("Failed to upload data to termbin.")
            sys.exit(1)
    except Exception as e:
        print(f"Error uploading to termbin: {e}")
        sys.exit(1)


def check_root() -> bool:
    if os.geteuid():
        print("This script must be run as root!", file=sys.stderr)
        return False
    return True


def main():
    # Commands to gather debug data
    ok = check_root()

    progs = {
        "inxi": "inxi",
        "eglinfo": "mesa-utils",
        "lsusb": "usbutils",
        "lspci": "pciutils",
    }

    for i in progs.keys():
        if not installed(i):
            prompt_install(progs[i])
            ok = False

    neofetch_installed = installed("neofetch")
    fastfetch_installed = installed("fastfetch")

    commands = [
        ["lspci"],
        ["lsusb"],
        ["lsusb -v"],
        ["sh", "-c", "ls /dev/ttyACM* /dev/ttyUSB* /dev/ttyS* 2>/dev/null || true"],
        ["inxi", "-ezrmxxfiv", "8"],
        ["env"],
        ["pacman", "-Q"],
    ]

    if fastfetch_installed:
        commands.append(["fastfetch", "--logo", "none", "--color", "0"])
    elif neofetch_installed:
        commands.append(["neofetch", "--off"])
    else:
        print(
            "Neither neofetch or fastfetch are installed! For a complete report, please install either."
        )

    commands.append(["dmesg"])  # Big, leave it last.

    if not ok:
        return

    # Run commands and gather outputs
    debug_data = "BredOS System Reporter v1.1\n"
    for cmd in commands:
        debug_data += f"\n=== Output of {' '.join(cmd)} ===\n"
        print(f"Running {' '.join(cmd)}\n")
        debug_data += run_command(cmd)

    # Upload data to termbin
    url = upload_to_termbin(debug_data)
    print(
        f"Debug data uploaded successfully: {url}Support: https://discord.gg/beSUnWGVH2"
    )
    print("That URL contains information about your system, which makes it easy for us to help you!")


if __name__ == "__main__":
    main()
