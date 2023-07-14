def main(*args, **kwargs):
    with open('scripts', 'rb+') as f:
        content = f.read()
        f.seek(0)
        f.write(content.replace(b'\r', b''))
        f.truncate()


if __name__ == "__main__":
    main()
