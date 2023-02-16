import os
import shutil
import time


def move_files():
    # getting the urls from user and formatting urls so we don't get an error
    user_source = input("Input url of the source folder: ")
    user_1_folder = user_source.replace(os.sep, "\\")  # changing os seperator to \\
    source_folder = os.path.join(user_1_folder, '')

    user_destination = input("Input url of the destination folder: ")
    destination_1_folder = user_destination.replace(os.sep, "\\")
    destination_folder = os.path.join(destination_1_folder, '')

    # Checking if urls are directories
    if os.path.isdir(source_folder) and os.path.isdir(destination_folder) == True:
        pass
    else:
        print("\n" + "One of the urls is invalid. Please check your urls again!")
        move_files()
    # for loop to list the files in the source folder
    for file_name in os.listdir(source_folder):
        source = source_folder + file_name
        if os.path.isfile(source):
            if file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
                image_dir = destination_folder + "Images"
                if os.path.isdir(image_dir):
                    shutil.move(source, image_dir)
                    print("File {} has been moved successfully to {}".format(file_name, image_dir))
                    time.sleep(1)
                else:
                    print("Folder Images is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(image_dir)
                    print("Folder Images has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, image_dir)
                    print("File {} has been moved successfully to {}".format(file_name, image_dir))
                    time.sleep(1)
            elif file_name.endswith(".mp4") or file_name.endswith(".avi") or file_name.endswith(".mov"):
                video_dir = destination_folder + "Videos"
                if os.path.isdir(video_dir):
                    shutil.move(source, video_dir)
                    print("File {} has been moved successfully to {}".format(file_name, video_dir))
                    time.sleep(1)
                else:
                    print("Folder Videos is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(video_dir)
                    print("Folder Videos has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, video_dir)
                    print("File {} has been moved successfully to {}".format(file_name, video_dir))
                    time.sleep(1)
            elif file_name.endswith(".mp3") or file_name.endswith(".aac") or file_name.endswith(".wav"):
                audio_dir = destination_folder + "Audio"
                if os.path.isdir(audio_dir):
                    shutil.move(source, audio_dir)
                    print("Fajli {} eshte bartur me sukses ne {}".format(file_name, audio_dir))
                    time.sleep(1)
                else:
                    print("Folder Audio is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(audio_dir)
                    print("Folder Audio has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, audio_dir)
                    print("File {} has been moved successfully to {}".format(file_name, audio_dir))
                    time.sleep(1)
            elif file_name.endswith(".exe"):
                software_dir = destination_folder + "Software"
                if os.path.isdir(software_dir):
                    shutil.move(source, software_dir)
                    print("Fajli {} eshte bartur me sukses ne {}".format(file_name, software_dir))
                    time.sleep(1)
                else:
                    print("Folder Software is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(software_dir)
                    print("Folder Software has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, software_dir)
                    print("File {} has been moved successfully to {}".format(file_name, software_dir))
                    time.sleep(1)
            elif file_name.endswith(".doc") or file_name.endswith(".txt") or file_name.endswith(".pdf"):
                documents_dir = destination_folder + "Documents"
                if os.path.isdir(documents_dir):
                    shutil.move(source, documents_dir)
                    print("Fajli {} eshte bartur me sukses ne {}".format(file_name, documents_dir))
                    time.sleep(1)
                else:
                    print("Folder Documents is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(documents_dir)
                    print("Folder Documents has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, documents_dir)
                    print("File {} has been moved successfully to {}".format(file_name, documents_dir))
                    time.sleep(1)
            elif file_name.endswith(".file"):
                other_dir = destination_folder + "Other"
                if os.path.isdir(other_dir):
                    shutil.move(source, other_dir)
                    print("Fajli {} eshte bartur me sukses ne {}".format(file_name, other_dir))
                    time.sleep(1)
                else:
                    print("Folder Other is not found, creating new folder")
                    time.sleep(1)
                    os.mkdir(other_dir)
                    print("Folder Other has been successfully created!")
                    time.sleep(1)
                    shutil.move(source, other_dir)
                    print("File {} has been moved successfully to {}".format(file_name, other_dir))
                    time.sleep(1)
            else:
                print("The found file {} is unknown!".format(file_name))
        else:
            print("{} is not a file".format(source))
    if len(os.listdir(source_folder)) == 0:
        print("\n" + "Files have been successfully moved!")
    else:
        for i in os.listdir(source_folder):
            print(f"File {i} is not moved, because is unknown")
            print("\n" + "Files have been successfully moved!")


move_files()
