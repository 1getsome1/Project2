import classes
import Project2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        p1 = classes.Point(2, 2)
        p2 = classes.Point(10, 10)
        rec = Project2.create_rectangle(p1, p2)
        tLeft = classes.Point(2, 10)
        bRight = classes.Point(10, 2)
        assert rec == classes.Rectangle(tLeft, bRight)

    def test_create_rectangle_2(self):
        p1 = classes.Point(23, 69)
        p2 = classes.Point(72, 34)
        rec = Project2.create_rectangle(p1, p2)
        tLeft = classes.Point(23, 69)
        bRight = classes.Point(72, 34)
        assert rec == classes.Rectangle(tLeft, bRight)

    # Part 2
    def test_shorter_duration_than_1(self):
        length1 = classes.Duration(2, 30)
        length2 = classes.Duration(8, 12)
        short = Project2.shorter_duration_than(length1, length2)
        assert short == True

    def test_shorter_duration_than_2(self):
        length1 = classes.Duration(181, 0)
        length2 = classes.Duration(195, 0)
        short = Project2.shorter_duration_than(length1, length2)
        assert short == True

    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = classes.Song("Decemberists", "June Hymn", classes.Duration(4, 30))
        song2 = classes.Song("Broken Bells", "October", classes.Duration(3, 40))
        song3 = classes.Song("Kansas", "Dust in the Wind", classes.Duration(3, 29))
        songs = [song1, song2, song3]
        length = classes.Duration(4, 0)
        s_song = [classes.Song("Broken Bells", "October", classes.Duration(3, 40)),
                  classes.Song("Kansas", "Dust in the Wind", classes.Duration(3, 29))]
        assert Project2.songs_shorter_than(songs, length) == s_song

    def test_songs_shorter_than_2(self):
        song1 = classes.Song("Yes", "Roundabout", classes.Duration(8, 35))
        song2 = classes.Song("Kendrick Lamar", "FEAR.", classes.Duration(7, 40))
        song3 = classes.Song("Tame Impala", "New Person, Same Old Mistakes", classes.Duration(6, 2))
        songs = [song1, song2, song3]
        length = classes.Duration(6, 0)
        s_song = []
        assert Project2.songs_shorter_than(songs, length) == s_song


    # Part 4
    def test_running_time_1(self):
        song1 = classes.Song("Decemberists", "June Hymn", classes.Duration(4, 30))
        song2 = classes.Song("Broken Bells", "October", classes.Duration(3, 40))
        song3 = classes.Song("Kansas", "Dust in the Wind", classes.Duration(3, 29))
        songs = [song1, song2, song3]
        playlist = [0, 1, 2]
        full = Project2.running_time(songs, playlist)
        assert full == classes.Duration(11, 39)

    def test_running_time_2(self):
        song1 = classes.Song("Yes", "Roundabout", classes.Duration(8, 35))
        song2 = classes.Song("Kendrick Lamar", "FEAR.", classes.Duration(7, 40))
        song3 = classes.Song("Tame Impala", "New Person, Same Old Mistakes", classes.Duration(6, 2))
        songs = [song1, song2, song3]
        playlist = [0, 1, 2, 1, 2, 0, 2]
        full = Project2.running_time(songs, playlist)
        assert full == classes.Duration(50, 36)

    def test_running_time_3(self):
        song1 = classes.Song("Yes", "Roundabout", classes.Duration(8, 35))
        song2 = classes.Song("Kendrick Lamar", "FEAR.", classes.Duration(7, 40))
        song3 = classes.Song("Tame Impala", "New Person, Same Old Mistakes", classes.Duration(6, 2))
        songs = [song1, song2, song3]
        playlist = [-4, 1, 3, 8, 2, 5, 2]
        full = Project2.running_time(songs, playlist)
        assert full == classes.Duration(19, 44)

    # Part 5
    def test_validate_route_1(self):
        link1 = ['san luis obispo', 'santa margarita']
        link2 = ['san luis obispo', 'pismo beach']
        link3 = ['atascadero', 'santa margarita']
        link4 = ['atascadero', 'creston']
        city_links = [link1, link2, link3, link4]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        assert Project2.validate_route(city_links, route) == True

    def test_validate_route_2(self):
        link1 = ['san luis obispo', 'santa margarita']
        link2 = ['san luis obispo', 'pismo beach']
        link3 = ['atascadero', 'santa margarita']
        link4 = ['atascadero', 'creston']
        city_links = [link1, link2, link3, link4]
        route = ['san luis obispo', 'santa margarita', 'creston']
        assert Project2.validate_route(city_links, route) == False

    # Part 6
    def test_longest_repetition_1(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        rep = Project2.longest_repetition(numbers)
        assert rep == 4

    def test_longest_repetition_2(self):
        numbers = [12, 3, 6, 8, 6, 7, 8, 9, 2, 12]
        rep = Project2.longest_repetition(numbers)
        assert rep == None

    def test_longest_repetition_3(self):
        numbers = [3, 3, 6, 8, 3, 3, 8, 9, 2, 12]
        rep = Project2.longest_repetition(numbers)
        assert rep == 0




if __name__ == '__main__':
    unittest.main()
