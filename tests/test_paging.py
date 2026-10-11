from app.paging import MAX_SIZE, paginate


def test_page_has_at_most_size_items():
    result = paginate(list(range(50)), page=1, size=20)
    assert len(result["items"]) == 20
    assert result["total"] == 50


def test_size_is_capped():
    assert paginate(list(range(500)), size=1000)["size"] == MAX_SIZE
