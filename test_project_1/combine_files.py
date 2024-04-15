import os

def combine_files(folder_path, output_file):
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 使用 os.walk() 遍历文件夹及其所有子文件夹
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # 循环遍历当前文件夹中的所有文件
            for filename in filenames:
                print("Processing filename: ", filename)
                # 检查文件扩展名是否为 .py 或 .txt
                if filename.endswith('.py') or filename.endswith('.txt'):
                    file_path = os.path.join(dirpath, filename)
                    # 确保路径是文件而不是目录
                    if os.path.isfile(file_path):
                        # 获取相对路径
                        relative_path = os.path.relpath(file_path, start=folder_path)
                        # 写入文件名和相对路径
                        outfile.write(f"Filename: {relative_path}\n")
                        # 打开并读取文件内容
                        with open(file_path, 'r', encoding='utf-8') as file:
                            contents = file.read()
                            outfile.write(contents)
                            outfile.write('\n')  # 在文件内容后添加换行符，以便分隔各个文件的内容


# 使用示例
folder_path = './voice_dialogue_system/'  # 替换为你的文件夹路径
output_file = './combined_output.txt'


combine_files(folder_path, output_file)
