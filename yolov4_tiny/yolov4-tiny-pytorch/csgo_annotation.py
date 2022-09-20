# 本来是可以直接用他的代码生成train需要的txt，但是我不想看他的代码
# 反正我知道目标是什么，所以我直接自己写了
import os
import sys
import random
from tkinter import image_names
import xml.etree.ElementTree as ET
import numpy as np
from utils.utils import get_classes

VOCdevkit_sets  = [('csgo', 'train'), ('csgo', 'valid'), ('csgo', 'test')]
classes_path        = 'F:\\repos\\CSGO_BIG\\code\\yolov4_tiny\\yolov4-tiny-pytorch\\model_data\\csgo.txt'
classes, _      = get_classes(classes_path)

photo_nums  = np.zeros(len(VOCdevkit_sets))
nums        = np.zeros(len(classes))
VOCdevkit_path  = 'F:\\repos\\CSGO_BIG\\code\\yolov4_tiny\\yolov4-tiny-pytorch\\VOCdevkit'

def convert_annotation(year, mode, image_id, list_file):
    in_file = open(os.path.join(VOCdevkit_path, 'VOC%s/%s/%s.xml'%(year, mode, image_id)), encoding='utf-8')
    
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0 
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        
        nums[classes.index(cls)] = nums[classes.index(cls)] + 1

if __name__ == "__main__":
    random.seed(0)
    for year, image_set in VOCdevkit_sets:
        # image_ids = open(os.path.join(VOCdevkit_path, 'VOC%s/ImageSets/Main/%s.txt'%(year, image_set)), encoding='utf-8').read().strip().split()
        # 构造出所有图片id的集合，但不包括后缀
        list_file = open('%s\\VOC%s\\%s_%s.txt'%(VOCdevkit_path,year,year, image_set), 'w', encoding='utf-8')
        VOC_csgo_path = os.path.join(VOCdevkit_path,"VOC%s\\%s"%(year,image_set))
        print(VOC_csgo_path)
        for i in os.listdir(VOC_csgo_path):
            if i.endswith(".jpg"):
                # total_xml.append(xml)
                list_file.write(VOC_csgo_path)
                list_file.write('\\%s'%i)
                convert_annotation(year, image_set,i[:-4], list_file)
                list_file.write('\n')
        # photo_nums[type_index] = len(image_ids)
        # type_index += 1
        list_file.close()