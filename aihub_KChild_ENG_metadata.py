

import os
import json
import pandas as pd

path = "D:\\012_KoreanChildSpokenEnglish\\01_data\\2_Validation\\labeling\\VL_eng_free_01\\eng_free"
a = os.listdir(path)

mdata = pd.read_csv("aihub_kchildeng_metadata.csv")
num = 1

for folder in os.listdir(path):
    NextFolder = path+"\\"+folder

    #print("nextfolder", NextFolder)
    for folder2 in os.listdir(NextFolder):
        NextFile = NextFolder + "\\" + folder2
        #print("nextfile", NextFile)

        for file in os.listdir(NextFile):
            file_path = NextFile + "\\" + file

            with open(file_path, 'r', encoding = "utf-8") as f:
                text = json.load(f)
                
                #print(json.dumps(text, indent = "\t"))

                sr = text['Wav']['SamplingRate']
                env = text['Environment']['NoiseEnviron']
                device = text['Environment']['RecordingDevices']
                spk_name = text['Speaker']['SpeakerName']
                spk_gender = text['Speaker']['Gender']
                spk_age = text['Speaker']['Age']
                spk_fluency = text['Speaker']['Fluency']
                spk_school = text['Speaker']['SchoolYear']
                file_name = text['File']['FileName']
                label = text['Transcription']['LabelText']

                mdata.loc[num] = [num, file_name, label, spk_name, spk_gender, spk_age, spk_fluency, spk_school, env, device, sr]

                num += 1
                
mdata.to_csv("aihub_kchildeng_metadata.csv")













                

