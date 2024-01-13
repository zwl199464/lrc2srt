import os
import re

def convert_lrc_to_srt(lrc_content):
    srt_content = ""
    lines = lrc_content.split("\n")
    for i, line in enumerate(lines):
        match = re.match(r"\(\d+):(\d+\.\d+\)", line)
        if match:
            minutes, seconds, text = match.groups()
            start_time = "{:02}:{:06.3f}".format(int(minutes), float(seconds))
            end_time = "00:00:00,000"
            if i + 1 < len(lines):
                next_match = re.match(r"\(\d+):(\d+\.\d+\)", lines[i + 1])
                if next_match:
                    next_minutes, next_seconds, _ = next_match.groups()
                    end_time = "{:02}:{:06.3f}".format(int(next_minutes), float(next_seconds))
            srt_content += "{}\n{} --> {}\n{}\n\n".format(i + 1, start_time.replace('.', ','), end_time.replace('.', ','), text)
    return srt_content

def convert_all_lrc_to_srt(directory):
    lrc_files = [file for file in os.listdir(directory) if file.endswith('.lrc')]
    for lrc_file in lrc_files:
        srt_file = os.path.splitext(lrc_file)[0] + '.srt'
        with open(os.path.join(directory, lrc_file), "r") as lrc_file:
            lrc_content = lrc_file.read()
        srt_content = convert_lrc_to_srt(lrc_content)
        with open(os.path.join(directory, srt_file), "w") as srt_file:
            srt_file.write(srt_content)
        print(f"Converted '{lrc_file}' to '{srt_file}'")
    print("Conversion complete!")

if __name__ == "__main__":
    directory = input("Enter the directory path where the .lrc files are located: ")
    while not os.path.isdir(directory):
        print("Invalid directory path. Please try again.")
        directory = input("Enter the directory path where the .lrc files are located: ")
    convert_all_lrc_to_srt(directory)
