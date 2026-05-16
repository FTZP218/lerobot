２号机器：
　主臂ttyACM12
　从臂ttyACM14

１号机器：
　主臂ttyACM13
　从臂ttyACM15

python -m lerobot.teleoperate \
    --robot.type=so100_follower \
    --robot.port=/dev/ttyACM14 \
    --robot.id=my_awesome_follower_arm \
    --teleop.type=so100_leader \
    --teleop.port=/dev/ttyACM12 \
    --teleop.id=my_awesome_leader_arm

# 数据采集
录制(正常)：
python -m lerobot.record \
    --robot.type=so100_follower \
    --robot.port=/dev/ttyACM14 \
    --robot.id=my_awesome_follower_arm \
    --robot.cameras="{top: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30}, laptop: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" \
    --teleop.type=so100_leader \
    --teleop.port=/dev/ttyACM12 \
    --teleop.id=my_awesome_leader_arm \
    --display_data=true \
    --dataset.num_episodes=23 \
    --dataset.episode_time_s=20 \
    --dataset.reset_time_s=6 \
    --dataset.root=/home/zhq2004/XArm/lerobot_smolvla/datasets/pick_place_pencil_smolvla \
    --dataset.repo_id=datasets/wwq_pencil \
    --dataset.single_task="Place the black pen inside the pen holder" \
    --dataset.push_to_hub=False \
    --resume=true




# 训练
python src/lerobot/scripts/train.py \
  --dataset.repo_id=task/pick1 \
  --policy.type=smolvla \
  --output_dir=outputs/train/smolvla_so100_test \
  --dataset.root=/home/zhq2004/XArm/lerobot_smolvla/datasets/pick_put_red \
  --job_name=smolvla_so100_test \
  --policy.device=cuda \
  --wandb.enable=false \
  --policy.vlm_model_name=/home/zhq2004/.cache/huggingface/hub/SmolVLM2-500M-Video-Instruct \
  --policy.push_to_hub=False    # 覆盖默认设置，跳过 Hub 上传验证

