from pathlib import Path


def get_files_info(working_directory, directory=None):
    if directory is None:
        return 'Error: "directory" argument is empty'

    # treat working_directory as truth
    resolved_dir_path = (Path(working_directory) / directory).resolve()
    working_dir_path = Path(working_directory).resolve()
    # treat directory input as relative path as working_dir is root "real" path
    if not resolved_dir_path.is_relative_to(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # check if directory is indeed a dir
    if not resolved_dir_path.is_dir():
        return f'Error: "{directory}" is not a directory'

    # Build and return string representing contents of directory
    """
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False
    """
    output = []
    for child in resolved_dir_path.iterdir():
        name = child.name  # Just the file or folder name
        is_dir = child.is_dir()
        size = child.stat().st_size
        output.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(output)
