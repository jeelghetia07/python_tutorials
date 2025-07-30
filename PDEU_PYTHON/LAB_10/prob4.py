import os
import shutil

os.makedirs('NewSubDir', exist_ok=True)
shutil.copy('OldSubDir/sample.txt', 'NewSubDir/sample.txt')
