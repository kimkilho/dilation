import os
import argparse
import random

random.seed(2016)


def parse_args():
    parser = argparse.ArgumentParser(description="Image/Label list generator")
    parser.add_argument("--imdb_name", dest="imdb_name", required=True,
                        help="Image DB name to be referenced")
    args = parser.parse_args()

    return args


def generate_image_label_list(img_dir, label_dir, image_sets_dir):
    # Read train filename_wo_ext list
    with open(os.path.join(image_sets_dir, "train.txt"), 'r') as fid:
        train_filename_wo_ext_list = [filename_wo_ext.strip()
                                      for filename_wo_ext in fid.readlines()]

    # Read valid filename_wo_ext list
    with open(os.path.join(image_sets_dir, "val.txt"), 'r') as fid:
        valid_filename_wo_ext_list = [filename_wo_ext.strip()
                                      for filename_wo_ext in fid.readlines()]

    # Write train/valid lists to image_list and label_list txt files
    with open("train_image_list.txt", 'w') as fid:
        for filename_wo_ext in train_filename_wo_ext_list:
            fid.write(os.path.join(img_dir, filename_wo_ext + ".jpg") + "\n")

    with open("train_label_list.txt", 'w') as fid:
        for filename_wo_ext in train_filename_wo_ext_list:
            fid.write(os.path.join(label_dir, filename_wo_ext + ".png") + "\n")

    with open("valid_image_list.txt", 'w') as fid:
        for filename_wo_ext in valid_filename_wo_ext_list:
            fid.write(os.path.join(img_dir, filename_wo_ext + ".jpg") + "\n")

    with open("valid_label_list.txt", 'w') as fid:
        for filename_wo_ext in valid_filename_wo_ext_list:
            fid.write(os.path.join(label_dir, filename_wo_ext + ".png") + "\n")

    print("Done")


def generate_cropped_image_label_list(img_dir, label_dir, val_portion=0.25):
    total_filename_list = sorted(os.listdir(img_dir))
    total_filename_wo_ext_list = [''.join(filename.split('.')[:-1])
                                  for filename in total_filename_list]

    total_size = len(total_filename_wo_ext_list)
    valid_size = int(total_size * val_portion)
    random.shuffle(total_filename_wo_ext_list)
    valid_filename_wo_ext_list = sorted(total_filename_wo_ext_list[:valid_size])
    train_filename_wo_ext_list = sorted(total_filename_wo_ext_list[valid_size:])

    # Write train/valid lists to image_list and label_list txt files
    with open("train_cropped_image_list.txt", 'w') as fid:
        for filename_wo_ext in train_filename_wo_ext_list:
            fid.write(os.path.join(img_dir, filename_wo_ext + ".jpg") + "\n")

    with open("train_cropped_label_list.txt", 'w') as fid:
        for filename_wo_ext in train_filename_wo_ext_list:
            fid.write(os.path.join(label_dir, filename_wo_ext + ".png") + "\n")

    with open("valid_cropped_image_list.txt", 'w') as fid:
        for filename_wo_ext in valid_filename_wo_ext_list:
            fid.write(os.path.join(img_dir, filename_wo_ext + ".jpg") + "\n")

    with open("valid_cropped_label_list.txt", 'w') as fid:
        for filename_wo_ext in valid_filename_wo_ext_list:
            fid.write(os.path.join(label_dir, filename_wo_ext + ".png") + "\n")

    print("Done")


if __name__ == "__main__":
    data_dir = "datasets"
    args = parse_args()

    imdb_name = args.imdb_name
    img_dir = os.path.join(data_dir, imdb_name, "JPEGImages")
    label_dir = os.path.join(data_dir, imdb_name, "SegmentationClass")
    image_sets_dir = os.path.join(data_dir, imdb_name, "ImageSets", "Segmentation")

    generate_image_label_list(img_dir, label_dir, image_sets_dir)

    # cropped_img_dir = os.path.join(img_dir, "sliding_cropped")
    # cropped_label_dir = os.path.join(label_dir, "sliding_cropped")
    #
    # generate_cropped_image_label_list(cropped_img_dir, cropped_label_dir)

