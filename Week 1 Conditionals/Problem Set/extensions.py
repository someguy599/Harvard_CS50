filename = input("File: ").split(".")

match filename[-1]:
    case "gif" | "txt" | "jpg" | "jpeg" | "png" | "pdf" | "zip":
        print(f"image/{filename[1]}")
    case _:
        print("application/octet-stream")