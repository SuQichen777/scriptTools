from PIL import Image
import os
import zipfile

def gif_to_png_zip(gif_path = 'localInput', output_dir='localOutput', zip_name='frames.zip'):
        
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    final_output_dir = os.path.join(script_dir, output_dir)
    # 构造绝对路径
    output_dir = os.path.join(final_output_dir, output_dir)
    zip_path = os.path.join(final_output_dir, zip_name)

    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 最后输出目录里会是：一个zip文件和若干png文件

    # 打开 gif 文件
    with Image.open(gif_path) as im:
        frame = 0
        while True:
            im.seek(frame)
            frame_path = os.path.join(output_dir, f'frame_{frame:03d}.png')
            im.convert('RGBA').save(frame_path, 'PNG')
            frame += 1
            try:
                im.seek(frame)
            except EOFError:
                break

    # 创建 zip 文件
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, output_dir))

    # 把最后输出的目录打印出来，只保留最后文件夹，不要前面的路径
    final_output_dir = os.path.relpath(final_output_dir, script_dir)
    print(f"Done! PNG frames saved in '{final_output_dir}' and zipped as '{zip_name}'")
    print(f"转换完成！PNG帧保存在 '{final_output_dir}' 中，并压缩为 '{zip_name}'")

while True:
    current_input = input("Please enter the gif file path (or 'exit' to quit): ")
    # 去除两端的单引号或者双引号
    current_input = current_input.strip().strip("'").strip('"')
    if current_input.lower() == 'exit':
        break
    else:
        # Call the function with the provided gif path
        print('Current input:', current_input)
        # check whether is empty
        # check whether exists
        if not os.path.exists(current_input):
            print("File does not exist, please try again.")
            continue
        # # check whether is gif
        if not current_input.lower().endswith('.gif'):
            print("File is not a gif, please try again.")
            continue
        gif_to_png_zip(current_input)
