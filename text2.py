from library_item import LibraryItem

def test_library_item_init():
    item = LibraryItem("Test Video", "Test Director", 3)
    assert item.name == "Test Video"
    assert item.director == "Test Director"
    assert item.rating == 3
    assert item.play_count == 0

def test_library_item_update():
    item = LibraryItem("Test Video", "Test Director", 3)
    item.rating = 5
    item.play_count += 1
    assert item.rating == 5
    assert item.play_count == 1
