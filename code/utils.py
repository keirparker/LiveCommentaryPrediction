import os
import soundfile
import unicodedata


def save_all_mp3_as_wav(directory_path, delete=False):
    # Function to resave all audio files to avoid formatting issues with sr
    def save_mp3_as_wav(file):
        data, samplerate = soundfile.read(file)
        soundfile.write(file[:-4] + '.wav', data, samplerate, subtype='PCM_16')
        if delete:
            delete_file(file_path=file)

    apply_to_all_files(directory_path, '.mp3', save_mp3_as_wav)


def delete_file(file_path):
    # Delete file
    os.remove(file_path)


def apply_to_all_files(root_dir, file_suffix, func):
    # Walk through the directory tree
    for root, dirs, files in os.walk(root_dir):
        # Loop through the files in the current directory
        for file in files:
            # Check if the file is an MP3 file
            if file.endswith(file_suffix):
                if not os.path.exists(os.path.join(root, file[:-4] + '.wav')):
                    # Apply the function to the file
                    func(os.path.join(root, file))
                    
                    
    
def normalize_string(string):
    # noramlize a given string
    return unicodedata.normalize('NFD', string).encode('ascii', 'ignore').decode('utf-8')