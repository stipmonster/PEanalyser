import pefile
# The List will contain all the extracted Unicode strings
#
strings = list()
def parseStringStruct(Ioffset,data,data_rva,pe,addToarray):
    lenght= int(pe.get_word_from_data(data[Ioffset:Ioffset+2], 0))
    Ioffset += 2
    
    stringLenght =int(pe.get_word_from_data(data[Ioffset:Ioffset+2], 0))
    #print stringLenght
    Ioffset += 2
    #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
    Ioffset += 2
    ustr = pe.get_string_u_at_rva(data_rva+Ioffset, max_length=30) # READING the 1 string
    key=ustr
    tempstring= ustr+ ",\""
    #print "key: " + str(len(ustr))
    Ioffset +=(len(ustr)*2)
    #print "first: " + str(offset)
    padding=int(lenght)-(int(stringLenght)*2)-(len(ustr)*2)-6
    #print "padding: " + str(padding)
    #padding=4
    Ioffset+=padding
    #print int(stringLenght)
    ustr = pe.get_string_u_at_rva(data_rva+Ioffset, max_length=stringLenght) # READING the 2 string
    data=ustr
    tempstring= tempstring + ustr+"\""
    Ioffset +=stringLenght*2
    #print "final: " + str(offset)
    addToarray(key,data)
    return Ioffset,tempstring

def info(): 
        return {"pluginName": "fileVersion", "Version": (0,1)}

    
# Fetch the index of the resource directory entry containing the strings
#
def start(filename,pe,addToarray):
    #pe =  pefile.PE(filename)
    try:
        rt_version_idx = [
            entry.id for entry in 
            pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_VERSION'])
    except:
        print "no info"
        return "no info"
    
    try:
        rt_version_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_version_idx]
    except AttributeError,ValueError:
        print "no info"
        return "no info"
        
    for entry in rt_version_directory.directory.entries:
        data_rva = entry.directory.entries[0].data.struct.OffsetToData
        size = entry.directory.entries[0].data.struct.Size
        #print 'Directory entry at RVA', hex(data_rva), 'of size', hex(size)
        offset=0
        data = pe.get_memory_mapped_image()[data_rva:data_rva+size] # reading the VS_VERSION_INFO
        #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
        offset += 2
        #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
        offset += 2
        #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
        offset += 2
        ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=17) # READING the string width "VS_VERSION_INFO"
        #print ustr
        offset+=17*2
        #print "dwSignature: " +  hex(pe.get_dword_from_data(data[offset:offset+4], 0)) #reading the VS_FIXEDFILEINFO
        offset+=4
        #print "dwStrucVersion: " +  hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileVersionMS: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileVersionLS: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwProductVersionMS: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwProductVersionLS: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileFlagMask: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileFlags: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileOS: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileType: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileSubtype: " + hex(pe.get_dword_from_data(data[offset:offset+4], 0))
        offset += 4
        #print "dwFileDateMS: " + hex(pe.get_dword_from_data(data[offset:offset+4],0))
        offset +=4
        #print "dwFileDateLS: " + hex(pe.get_dword_from_data(data[offset:offset+4],0))
        offset +=4
        stringarraylenght=int(pe.get_word_from_data(data[offset:offset+2],0))
        totallenghtchildren=offset+stringarraylenght
        #print "StringFilelength: " + str(stringarraylenght)
        offset +=2 
        #print "always 0: " + hex(pe.get_word_from_data(data[offset:offset+2],0))
        offset +=2 
        #print "type: " + hex(pe.get_word_from_data(data[offset:offset+2],0))
        offset +=2 
        
        #print hex(pe.get_word_from_data(data[offset:offset+2],0))
        #offset +=2
        ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=15) # READING the string width "StringFileInfo"
        #print ustr
        offset+=15*2
        lenghtstrings = int(pe.get_word_from_data(data[offset:offset+2], 0))
        totallenghtstrings=lenghtstrings+offset-2
        #print lenghtstrings
        offset += 2
        #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
        offset += 2
        #print hex(pe.get_word_from_data(data[offset:offset+2], 0))
        offset += 2
        ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=8) # READING unicodetype??
        #print ustr
        offset+=8*2
        offset+=2#padding
        #print totallenghtstrings
        returnString= "## version data"
        while(offset < totallenghtstrings):
            offset,tempstring = parseStringStruct(offset,data,data_rva,pe,addToarray)
            returnString=returnString+tempstring
            offset += offset%4
    return returnString