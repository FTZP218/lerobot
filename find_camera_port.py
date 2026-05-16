"""
    测试使用：调试摄像头位置使用！！
"""

import cv2
import os
import sys
from src.lerobot.cameras.opencv import OpenCVCamera , find_cameras

def test_camera(camera_id, window_name="Camera Preview"):
    """测试并显示单个摄像头画面"""
    try:
        # 初始化摄像头
        cam = cv2.VideoCapture(camera_id)
        if not cam.isOpened():
            print(f"无法打开摄像头 {camera_id}")
            return False
        
        # 显示操作提示
        print(f"\n正在测试摄像头 {camera_id}:")
        print("  - 按 'n' 切换到下一个摄像头")
        print("  - 按 'q' 退出程序")
        
        while True:
            ret, frame = cam.read()
            if not ret:
                print(f"摄像头 {camera_id} 读取帧失败")
                break
            
            # 显示画面
            cv2.imshow(window_name, frame)
            
            # 按 'q' 退出当前摄像头，'n' 切换到下一个
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                return False  # 退出整个程序
            elif key == ord('n'):
                return True  # 切换到下一个摄像头
        
        return False  # 默认退出
    
    except Exception as e:
        print(f"摄像头 {camera_id} 发生错误: {e}")
        return False
    
    finally:
        cam.release()
        cv2.destroyWindow(window_name)

def main():
    # 初始提示
    print("欢迎使用摄像头测试程序！")
    print("操作说明：请你将鼠标光标点击弹出图像然后按照下面提示切换摄像头")
    print("  - 按 'n' 切换到下一个摄像头")
    print("  - 按 'q' 随时退出程序")
    print("正在搜索可用摄像头...\n")
    
    # 查找所有可用摄像头
    try:
        camera_infos = find_cameras()
    except Exception as e:
        print(f"查找摄像头失败: {e}")
        return
    
    camera_ids = [cam["index"] for cam in camera_infos]
    
    if not camera_ids:
        print("未找到任何可用摄像头")
        return
    
    print(f"找到以下摄像头端口: {camera_ids}")
    print(f"共检测到 {len(camera_ids)} 个摄像头，开始测试...\n")
    
    # 依次测试每个摄像头
    for idx, cam_id in enumerate(camera_ids):
        window_name = f"Camera {cam_id} Preview"
        continue_testing = test_camera(cam_id, window_name)
        if not continue_testing:
            break  # 用户按 'q' 或发生错误，退出循环
    
    print("\n所有摄像头测试完成或已退出")

if __name__ == "__main__":
    main()

    


