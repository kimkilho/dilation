LD_LIBRARY_PATH=caffe-dilation/build_master/lib PYTHONPATH=caffe-dilation/build_master/python \
  python test.py frontend \
  --work_dir training \
  --image_list val_image_list.txt \
  --bin_list val_image_list.txt \
  --bin \
  --mean [70, 74, 84] \
  --weights training/snapshots/frontend_vgg_iter_124000.caffemodel \
  --classes 2

