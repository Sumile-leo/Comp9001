def apollo(count):
    print("Guidance is internal.")
    for i in range(count, -1, -1):
        if i == 6:
            print("Ignition sequence start.")
        if i == 0:
            print("All engine running.\nLift off on Apollo 11!")
            break
        print(f"{i}...")

apollo(12)