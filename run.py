import os
import subprocess
import glob

GPU_ID = "0"
MODEL_DIR = "./esrgan/models"
INPUT_DIR = "./input/*.*"
OUT_DIR = "./output"
MODEL = "realesrgan-x4plus"
CMD = "./esrgan/realesrgan-ncnn-vulkan.exe"


def main():
    files = glob.glob(INPUT_DIR)
    for a in files:
        fname = os.path.basename(a)
        print("process: "+fname)
        subprocess.run([CMD,"-i",a, "-o", os.path.join(OUT_DIR, fname), "-n", MODEL, "-g ", GPU_ID])
 

if __name__ == "__main__":
    main()
