import os


def write_file_tree(file_path):
    with open(file_path, 'w') as f:
        for root, dirs, files in os.walk('.'):
            level = root.replace('.', '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            for file in files:
                f.write(f'{indent}    {file}\n')


write_file_tree('game_architecture.txt')
