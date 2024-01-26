#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    importnames = dir(hidden_4)
    for name in importnames:
        if name[:2] == "__":
            continue
        print(name)
