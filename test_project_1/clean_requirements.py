import subprocess
import re


def clean_requirements():
    # 运行 pip freeze 并捕获输出
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True)

    # 拆分输出以获取单独的行
    lines = result.stdout.split('\n')

    cleaned_lines = []
    for line in lines:
        # 只提取包名和版本号
        match = re.match(r'([a-zA-Z0-9\-_]+)==([0-9\.]+)', line)
        if match:
            cleaned_lines.append(f'{match.group(1)}=={match.group(2)}')

    # 将清理后的依赖写入新的 requirements.txt 文件
    with open('requirements_clean.txt', 'w') as f:
        for line in cleaned_lines:
            f.write(line + '\n')


clean_requirements()
