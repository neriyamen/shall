from format import *
import struct
import zipfile
import os

class FILE:
    # trunsfer files between client and socket with zip option

    def unpack_file_properties(self, data):
        # the file is coming pack with properties. this function parser the packing.
        (path_len,) = struct.unpack('>i', data[:4])
        path = data[4:4 + path_len]
        (data_len,) = struct.unpack('>i', data[4 + path_len:8 + path_len])
        return path.decode('utf-8'), data_len

    def pack_file_properties(self, path, new_path):
        # create package of file data and file's properties.
        zip_file = self.zip_file(path, new_path)
        return struct.pack(f'>I{len(new_path)}sI',
                           len(new_path), new_path.encode(), len(zip_file)), zip_file

    def create_file(self, path, zip_data):
        # take a zipped file data and create a file
        file_data = self.unzip_file(path, zip_data)
        with open(path, 'wb') as file:
            file.write(file_data)

    def zip_file(self, path, new_path):
        # zipper files
        zip_file = zipfile.ZipFile(path + '.zip', mode='w')
        try:
            zip_file.write(path, new_path.split('\\')[-1])
            zip_file.close()
            with open(path + '.zip', 'rb') as zip_file:
                zip_data = zip_file.read()
                zip_file.close()
                self.remove_file(path + '.zip')
            return zip_data
        finally:
            zip_file.close()

    def unzip_file(self, path, zip_data):
        # unzip files
        with open(path + '.zip', 'wb') as file:
            file.write(zip_data)
            file.close()
        zf = zipfile.ZipFile(path + '.zip')
        try:
            file_data = zf.read(path.split('\\')[-1])
            return file_data
        except KeyError:
            print('ERROR: Did not find %s in zip file' % path)
        finally:
            zf.close()
            try:
                self.remove_file(path + '.zip')
            except:
                print('cant remove zip file')

    @staticmethod
    def remove_file(path):
        # remove file by path
        try:
            os.remove(path)
        except:
            print('failed remove file:', path)
