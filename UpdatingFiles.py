import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                print(local_path)
                relative_path = os.path.relpath(local_path, file_from)
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'H5MlzHMkbDEAAAAAAAAAAZoEZ2CNGMgVP51oUy1i27ER_5p_i-XTNlGT5o4Fw-sY'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the destination file: ")
    transferData.uploadFiles(file_from, file_to)

    print("File has been moved!")

main()