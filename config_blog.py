def config(val, default):
    try:
             
        return globals()[val]
    except KeyError:
        return default

def set_config():
    global  bloglocaladdress,history
    bloglocaladdress="/home/mrrobot/Desktop/blog/"
    history="/home/mrrobot/Desktop/blog/file_history.json"
set_config()  
 
