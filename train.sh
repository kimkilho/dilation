# export CAFFE_DILATION_BUILD=./caffe-dilation
# export LD_LIBRARY_PATH=${CAFFE_DILATION_BUILD}/build_master/lib:${LD_LIBRARY_PATH}
# export PYTHONPATH=${CAFFE_DILATION_BUILD}/bulid_master/python:${PYTHONPATH}
# export LD_LIBRARY_PATH=${CAFFE_DILATION_BUILD}/build_master/lib:${LD_LIBRARY_PATH}
# export PYTHONPATH=${CAFFE_DILATION_BUILD}/bulid_master/python:${PYTHONPATH}
LD_LIBRARY_PATH=caffe-dilation/build_master/lib PYTHONPATH=caffe-dilation/build_master/python \
  python train.py frontend \
  --work_dir training \
  --train_image train_image_list.txt \
  --train_label train_label_list.txt \
  --test_image val_image_list.txt \
  --test_label val_label_list.txt \
  --mean [70, 74, 84] \
  --train_batch 6 \
  --test_batch 2 \
  --caffe caffe-dilation/build_master/tools/caffe \
  --weights pretrained/vgg_conv.caffemodel \
  --crop_size 500 \
  --classes 2 \
  --lr 0.001 \
  --momentum 0.9

