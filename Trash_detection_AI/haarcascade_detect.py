import subprocess

# Setup Path
WORKSPACE_PATH = 'C:\SGU\Python\RealTimeObjectDetection\Tensorflow\workspace'
SCRIPT_PATH = 'C:\SGU\Python\RealTimeObjectDetection\Tensorflow\scripts'
APIMODEL_PATH = 'C:\SGU\Python\RealTimeObjectDetection\Tensorflow\models'
ANNOTATION_PATH = WORKSPACE_PATH + '/annotations'
IMAGE_PATH = WORKSPACE_PATH + '\images'
MODEL_PATH = WORKSPACE_PATH + '\models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH + '/pre-trained-models'
CONFIG_PATH = MODEL_PATH + '/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH + '/my_ssd_mobnet/'


#Create LabelMap

# Array label
labels = [{'name':'Water-Bottle', 'id':1}, {'name':'Normal-Object', 'id':2}]

#write label
with open(rf'{WORKSPACE_PATH}\annotations\label_map.pbtxt', 'w') as f:
    #create loop in these labels
    for label in labels:
        f.write('item{\n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

#Create TF record

subprocess.run(['python', SCRIPT_PATH + '/generate_tfrecord.py', '-x', IMAGE_PATH + '/train', '-l', ANNOTATION_PATH + '/label_map.pbtxt', '-o', ANNOTATION_PATH + '/train.record'])
#if labels == True: 
#    print('it is working')
#else:
#    print('Nope')