CUDA_VISIBLE_DEVICES=0 python inference.py --model deeplabv3plus_resnet101 \
--checkpoint_path /data/danshili/suctionnet_model/realsense-deeplabplus-RGBD \
--split graspnerf \
--camera realsense \
--dataset_root /home/danshili/ours-graspnerf/my_graspnerf/src/nr/tmp/img \
--depth_dir /data/danshili/merged_graspnerf/debug/2023-09-03-03-21-35 \
--save_dir /data/danshili/suctionnet_out/graspnerf \
--save_visu