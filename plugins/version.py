import pefile
pe =  pefile.PE("/Users/Erik/Downloads/idafree50.exe")
# The List will contain all the extracted Unicode strings
#
strings = list()

# Fetch the index of the resource directory entry containing the strings
#
rt_version_idx = [
  entry.id for entry in 
  pe.DIRECTORY_ENTRY_RESOURCE.entries].index(pefile.RESOURCE_TYPE['RT_VERSION'])

rt_version_directory = pe.DIRECTORY_ENTRY_RESOURCE.entries[rt_version_idx]

for entry in rt_version_directory.directory.entries:
    data_rva = entry.directory.entries[0].data.struct.OffsetToData
    size = entry.directory.entries[0].data.struct.Size
    print 'Directory entry at RVA', hex(data_rva), 'of size', hex(size)
    offset=0
    data = pe.get_memory_mapped_image()[data_rva:data_rva+size]
    print hex(pe.get_word_from_data(data[offset:offset+2], 0))
    offset += 2
    print hex(pe.get_word_from_data(data[offset:offset+2], 0))
    offset += 2
    print hex(pe.get_word_from_data(data[offset:offset+2], 0))
    offset += 2
    ustr = pe.get_string_u_at_rva(data_rva+offset, max_length=17)
    print ustr
    offset+=17*2
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset+=4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    print hex(pe.get_dword_from_data(data[offset:offset+4], 0))
    offset += 4
    