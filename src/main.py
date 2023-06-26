import music_handler


def main():
    music = music_handler.Music("Wanderer's love song", 'Wu Bai', '1994-12-16')
    music.print_info()

if __name__ == '__main__':
    main()