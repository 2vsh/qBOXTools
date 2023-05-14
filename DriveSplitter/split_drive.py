import subprocess

def split_drive(drive_letter, new_partition_size_gb):
    diskpart_script = f"""
    list volume
    select volume {drive_letter}
    shrink desired={new_partition_size_gb * 1024}
    create partition primary
    assign
    format fs=ntfs quick
    exit
    """

    with open("diskpart_script.txt", "w") as script_file:
        script_file.write(diskpart_script)

    try:
        print("Running diskpart script...")
        subprocess.run(["diskpart", "/s", "diskpart_script.txt"], check=True)
        print("Drive successfully split.")
    except subprocess.CalledProcessError:
        print("Error: Unable to split the drive. Please make sure you have administrative privileges.")
    finally:
        subprocess.run(["del", "diskpart_script.txt"], shell=True)

if __name__ == "__main__":
    drive_letter = input("Enter the drive letter to split (e.g., 'C'): ")
    new_partition_size_gb = int(input("Enter the new partition size in GB: "))

    split_drive(drive_letter.upper(), new_partition_size_gb)
