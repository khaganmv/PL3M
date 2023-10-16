import os
import subprocess
import shutil
import threading

WEM = 'wem\\'
OUT = 'out\\'

def wem_to_archive(file):
    title = file.split('_')[0]
    path = os.path.join(title, 'base', 'sound', 'soundbanks')
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    shutil.copyfile(WEM + file, path + '/749435057.wem')
    subprocess.call(['.\\wolven_kit_cli\\net5.0-windows\\WolvenKit.CLI', 'pack', '-p', title], stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
    shutil.rmtree(title)

threads = []

for file in os.listdir(WEM):
    thread = threading.Thread(target=wem_to_archive, args=(file,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()

for file in os.listdir('.'):
    if 'basegame' in file:
        shutil.copyfile(file, OUT + file.split('_')[1])
        os.remove(file)
