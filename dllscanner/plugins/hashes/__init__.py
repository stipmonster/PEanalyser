def info(): 
        return {"pluginName": "hashes", "Version": (0,1)}


def start(filename,pe):
    return "md5:" + pe.get_hash_md5() + "\n" + "sha1:" + pe.get_hahs_sha1() + "\n" + "sha265:" + pe.get_hash_sha256() + "\n" + "sha512:" + pe.get_hash_sha512() + "\n"