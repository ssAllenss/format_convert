import os
from pydub import AudioSegment


def m4a2wav(filepath: str, if_remove=False):
    status, error = 0, 0
    filetype, dirpath, filename, wav_filename, wav_path = "", "", "", "", ""
    try:
        filetype = filepath.rsplit('.')[-1]
        dirpath = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        
        track = AudioSegment.from_file(filepath, filetype)
        wav_filename = filename.replace(filetype, 'wav')
        wav_path = os.path.join(dirpath, wav_filename)
        file_handle = track.export(wav_path, format='wav')
        if if_remove:
            os.remove(filepath)   

        status = 1
    except Exception(error):
        pass
    finally:
        status_info = "Success" if status else "Failed"
        print(f"==Input File Path: {filepath}",
            f"==Input File Name: {filename}",
            f"==Output File Name: {wav_filename}",
            f"==Output File Path: {wav_path}",
            f"==If Remove Input File: {if_remove}",
            f"==Convert: : {status_info}",
            "==Error Info: " if not status else "",
             sep="\n")


if __name__ == "__main__":
    filepath = "C:\\Users\\11449\\Documents\\Sound recordings\\Recording.m4a"
    m4a2wav(filepath)
