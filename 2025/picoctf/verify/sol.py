def sol():
    return "find ./files -type f | xargs -I {} ./decrypt.sh {}"