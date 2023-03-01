import glob, os,subprocess
parent_dir = "."
absolute_path = os.path.dirname(__file__)
print ("#########################################")
print ("Reading all file .....")

sub_folders = [name for name in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, name))]
#print(sub_folders)
for folder in sub_folders:
  sub_folders_2 = [name for name in os.listdir(parent_dir+"\\"+folder) if os.path.isdir(os.path.join(parent_dir+"\\"+folder, name))]
  #print(sub_folders_2)
  for folder_2 in sub_folders_2:
    print (folder_2)
    command = 'cmd /k ffmpeg -i "'
    for media_file in glob.glob(os.path.join(parent_dir+"\\"+folder+"\\"+folder_2, '*.media')):
      print ("Reading : "+absolute_path+media_file[1:])
      command = command + 'concat:'+absolute_path+media_file[1:]+'|'
    print ("")
    print ("#########################################")
    print ("send command to ffmpeg..")
    command = command[:len(command)-1]
    command = command + '" -c copy '+parent_dir[1:]+"_"+folder+"_"+folder_2+'_out.mp4'
    #process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    #process.wait()
    process = subprocess.Popen(command)
    import time
    time.sleep(0) 
 


