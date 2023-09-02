CUDA_VISIBLE_DEVICES=0 python inference.py --model deeplabv3plus_resnet101 \
--checkpoint_path /data/danshili/suctionnet_model/realsense-deeplabplus-RGBD \
--split test_seen \
--camera realsense \
--dataset_root /data/danshili/suctionnet_data \
--save_dir /data/danshili/suctionnet_out \
--save_visu

