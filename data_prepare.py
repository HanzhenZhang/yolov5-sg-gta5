import shutil

root_target = '/mnt/ssd/zw/yolov5-sg/datasets/gta5/images'
root_original = '/mnt/ssd/zw/gta5/images'
total = 24966
train_rate = 0.8
test_rate = 0.2
index = int(total * train_rate)
# print(index)
# split train file
for i in range(1, 2976):
    i = str(i)
    file_name = "0" * (5 - len(i)) + i + ".png"
    original = root_original + "/" + file_name
    target = root_target + "/" + "train"
    shutil.copy(original, target)
# split test file
for i in range(2976, 3476):
    i = str(i)
    file_name = "0" * (5 - len(i)) + i + ".png"
    original = root_original + "/" + file_name
    target = root_target + "/" + "val"
    shutil.copy(original, target)
