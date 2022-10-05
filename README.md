# Download Datasets

https://www.cityscapes-dataset.com/

# Prepare Training Label

1. Download cityscapesScripts https://github.com/mcordts/cityscapesScripts
2. Modify 'cityscapesPath' in 'cityscapesScripts/cityscapesscripts/preparation/createTrainIdLabelImgs.py'
3. Run python createTrainIdLabelImgs.py

# Train
1. Modify 'path' in 'yolov5-sg\data\cityscapes.yaml'
2. Modify --data, --batch-size, --device ... in parse_opt of 'yolov5-sg\train.py'
3. python train.py (single GPU), python -m torch.distributed.run --nproc_per_node N train.py --sync-bn (N GPUs)