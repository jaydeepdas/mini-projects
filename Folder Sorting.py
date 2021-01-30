import os,shutil
folders={
    'videos':['.mp4','.MKV'],
    'audios':['.wav','.mp3'],
    'images':['.jpg','.png'],
    'documents':['.doc','.xlsx','.xls','.pdf','.zip','.rar','.docx','.webp'],
}
 #print(folders)
 #for folder_name in folders:
     #print(folder_name,folders[folder_name])

def create_move(ext,file_name):
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
            break
  
directry=input("Enter the Location:")
all_files=os.listdir(directry)
#print(all_files)
for i in all_files:
    if os.path.isfile(os.path.join(directry,i) )==True:
        create_move(i.split(".")[-1],i)
