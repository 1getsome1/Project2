import classes

# Write your functions for each part in the space below.

# Part 1
# design Recipe:
# 1) takes two points and turns them into points that can be for a rectangle
# 2) create_rectangle(p1: Point, p2: Point)->Rectangle:
# 3) template of function
#     - get both x coordinates from each point
#     - get both y coordinates from each point
#     - set the lowest value of x to the top left point
#     - set the highest value of x to the bottom right point
#     - set the highest value of y to the top left point
#     - set the lowest value of y to the bottom right point
# 4) test case:    def test_create_rectangle_1(self):
#                      p1 = classes.Point(2, 2)
#                      p2 = classes.Point(10, 10)
#                      rec = Project2.create_rectangle(p1, p2)
#                      tLeft = classes.Point(2, 10)
#                      bRight = classes.Point(10, 2)
#                      assert rec == classes.Rectangle(tLeft, bRight)
# 5)

def create_rectangle(p1: classes.Point, p2: classes.Point)->classes.Rectangle:
    x_coord = [p1.x, p2.x]
    y_coord = [p1.y, p2.y]
    l_x, r_x = min(x_coord), max(x_coord)
    l_y, r_y = max(y_coord), min(y_coord)
    top_L = classes.Point(l_x, l_y)
    bottom_R = classes.Point(r_x, r_y)
    return classes.Rectangle(top_L, bottom_R)


# Part 2
# design Recipe:
# 1) check if the given duration is less than another duration
# 2) shorter_duration_than(first: Duration, second: Duration)->bool:
# 3) template of function
#     - check if the first duration is shorter than the second duration return true
#     - if it isn't then check if the seconds for first is smaller than second then return true
# 4) test case:    def test_shorter_duration_than_1(self):
#                      length1 = classes.Duration(2, 30)
#                      length2 = classes.Duration(8, 12)
#                      short = Project2.shorter_duration_than(length1, length2)
#                      assert short == True
# 5)

def shorter_duration_than(first: classes.Duration, second: classes.Duration)-> bool:
    if first.minutes < second.minutes:
        return True
    elif first.minutes == second.minutes and first.seconds < second.seconds:
        return True
    else:
        return False

# Part 3
# design Recipe:
# 1) create a new list of songs that have a shorter length
# 2) songs_shorter_than(songs: list[Song], length: Duration)->list[Song]
# 3) template of function
#     - check if the length of the list is equal to 0
#     - make new list
#     - cycle through the list of songs
#     - check if each song is less than the length
#     - put each song that is lower than the length into teh new list
# 4) test case:    def test_songs_shorter_than_2(self):
#                      song1 = classes.Song("Yes", "Roundabout", classes.Duration(8, 35))
#                      song2 = classes.Song("Kendrick Lamar", "FEAR.", classes.Duration(7, 40))
#                      song3 = classes.Song("Tame Impala", "New Person, Same Old Mistakes", classes.Duration(6, 2))
#                      songs = [song1, song2, song3]
#                      length = classes.Duration(6, 0)
#                      s_song = []
#                      assert Project2.songs_shorter_than(songs, length) == s_song
# 5)

def songs_shorter_than(songs: list[classes.Song], length: classes.Duration)->list[classes.Song]:
    if len(songs) == 0:
        return []
    filter_l = []
    for x in songs:
        if x.duration.minutes < length.minutes:
            filter_l.append(x)
        elif x.duration.minutes == length.minutes and x.duration.seconds < length.seconds:
            filter_l.append(x)
    return filter_l



# Part 4
# design Recipe:
# 1) count up each song's duration from the playlist from the list
# 2) running_time(songs: list[Song], playlist: list[int])->Duration:
# 3) template of function
#     - make an empty duration variable, total_d
#     - cycle through the playlist
#     - use the numbers from playlist as an index to access the songs in the song list
#     - add the minutes of the song to total_d
#     - add the seconds of the song to total_d
#     - an if statement that stops seconds from being over or equal to 60
# 4) test case:    def test_running_time_2(self):
#                      song1 = classes.Song("Yes", "Roundabout", classes.Duration(8, 35))
#                      song2 = classes.Song("Kendrick Lamar", "FEAR.", classes.Duration(7, 40))
#                      song3 = classes.Song("Tame Impala", "New Person, Same Old Mistakes", classes.Duration(6, 2))
#                      songs = [song1, song2, song3]
#                      playlist = [0, 1, 2, 1, 2, 0, 2]
#                      full = Project2.running_time(songs, playlist)
#                      assert full == classes.Duration(50, 36)
# 5)

def running_time(songs: list[classes.Song], playlist: list[int])->classes.Duration:
    total_d = classes.Duration(0, 0)
    for x in playlist:
        if 0 <= x < len(songs):
            total_d.minutes += songs[x].duration.minutes
            total_d.seconds += songs[x].duration.seconds
        if total_d.seconds >= 60:
            total_d.minutes += total_d.seconds // 60
            total_d.seconds = total_d.seconds % 60
    return total_d

# Part 5
# design Recipe:
# 1) checks if the specified route is possible with the given list of routes
# 2) validate_route(links: list[list[str]], route: list[str])
# 3) template of function
#     - if the length of route is equal to 0 or 1 then its true
#     - use the range of the length of route to cycle through the lists
#     - if the route is not in the list of links then its false
#     - otherwise return true
# 4) test case:    def test_validate_route_1(self):
#                      link1 = ['san luis obispo', 'santa margarita']
#                      link2 = ['san luis obispo', 'pismo beach']
#                      link3 = ['atascadero', 'santa margarita']
#                      link4 = ['atascadero', 'creston']
#                      city_links = [link1, link2, link3, link4]
#                      route = ['san luis obispo', 'santa margarita', 'atascadero']
#                      assert Project2.validate_route(city_links, route) == True
# 5)

def validate_route(links: list[list[str]], route: list[str]):
    if len(route) == 0 or len(route) == 1:
        return True
    for x in range(len(route)-1):
        if [route[x], route[x+1]] not in links and [route[x+1], route[x]] not in links:
            return False
    return True

# Part 6
# design Recipe:
# 1) get the index were the longest repetition in a list of integers starts
# 2) longest_repetition(nums: list[int]):
# 3) template of function
#     - check if the length of the list is 0
#     - make three variables with two of them equal to 0 and the last one equal to 1
#     - make a for loop for the range of the length of the list starting at one
#     - if the current number is the same as the next one then check if it's greater than the current max length
#     - then make max start equal to start
#     - also make the max length equal to the index minus start
#     - if max length stays 1 then return none
# 4) test case:          def test_longest_repetition_2(self):
#                            numbers = [12, 3, 6, 8, 6, 7, 8, 9, 2, 12]
#                            rep = Project2.longest_repetition(numbers)
#                            assert rep == None
# 5)

def longest_repetition(nums: list[int]):
    if len(nums) == 0:
        return None
    start = 0
    m_start = 0
    m_len = 1
    for x in range(1, len(nums)):
        if nums[x] == nums[start]:
            if x - start + 1 > m_len:
                m_start = start
                m_len = x - start + 1
        else:
            start = x
    if m_len == 1:
        return None
    else:
        return m_start


