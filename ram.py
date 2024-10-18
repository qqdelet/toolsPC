import wmi

def get_memory_info():
    c = wmi.WMI()
    memory_info = []
    
    for memory in c.Win32_PhysicalMemory():
        memory_details = {
            "Capacity (MB)": int(memory.Capacity) // (1024**2), 
            "Type": memory.MemoryType, 
            "Speed (MHz)": memory.Speed,  
            "Manufacturer": memory.Manufacturer,
        }
        memory_info.append(memory_details)
    
    return memory_info

memory_info = get_memory_info()
for idx, mem in enumerate(memory_info, start=1):
    print(f"Модуль пам'яті {idx}:")
    print(f"  Ємність: {mem['Capacity (MB)']} MB")
    print(f"  Тип: {mem['Type']}")
    print(f"  Частота: {mem['Speed (MHz)']} MHz")
    print(f"  Виробник: {mem['Manufacturer']}")
