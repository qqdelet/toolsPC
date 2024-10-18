import wmi

def get_memory_timings():
    c = wmi.WMI()
    for memory in c.Win32_PhysicalMemory():
        print(f"Manufacturer: {memory.Manufacturer}")
        print(f"Part Number: {memory.PartNumber.strip()}")
        print(f"Capacity: {int(memory.Capacity) // (1024 ** 2)} MB")
        print(f"Speed: {memory.Speed} MHz")
        print(f"Memory Type: {memory.MemoryType}")

