from pymediainfo import MediaInfo

def test():
    mi = MediaInfo.parse('a.mkv')
    print(mi.tracks)
    print(mi.to_data())

    print('---')
    for el in mi.tracks:
        print(el.to_data())



def test2():
    mi=MediaInfo.parse('a.mkv')
    print(mi.to_data())


test2()