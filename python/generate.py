import os
import pathlib
import shutil

from grpc_tools.protoc import main


IN_DIR = pathlib.Path('../protos/')
OUT_DIR = pathlib.Path('./heekkr/')


if __name__ == '__main__':
    shutil.rmtree(OUT_DIR, ignore_errors=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    
    proto_files = [
        f
        for base, _, files in os.walk(IN_DIR)
        for f in files
        if os.path.splitext(f)[-1].lower() == ".proto"
    ]
    opts = [
        '',
        '-I',
        str(IN_DIR),
        '--python_out',
        str(OUT_DIR),
        '--grpc_python_out',
        str(OUT_DIR),
        *proto_files,
    ]
    main(opts)

    (OUT_DIR / "__init__.py").touch()
