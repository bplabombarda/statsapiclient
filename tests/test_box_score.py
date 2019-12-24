from statsapiclient.box_score import BoxScore

mock_data = {
    "where": "is",
    "the": "data?"
}


class TestBoxScore:
    def test_instantiate_box_score(self):
        box_score = BoxScore(mock_data)

        assert box_score.data == mock_data
