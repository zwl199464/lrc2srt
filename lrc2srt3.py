import os
import pylrc

def convert_lrc_to_srt(lrc_file_path, srt_file_path):
    with open(lrc_file_path, 'r', encoding='utf-8') as lrc_file:
        lrc_string = ''.join(lrc_file.readlines())

    subs = pylrc.parse(lrc_string)
    srt_string = subs.toSRT()  # convert lrc to srt string

    with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
        srt_file.write(srt_string)

def main():
    for filename in os.listdir('.'):
        if filename.endswith('.lrc'):
            lrc_file_path = filename
            srt_file_path = filename.replace('.lrc', '.srt')
            convert_lrc_to_srt(lrc_file_path, srt_file_path)

if __name__ == "__main__":
    main()
