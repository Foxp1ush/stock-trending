import unittest

from src import ticker_extractor


class TickerExtractorTest(unittest.TestCase):
    def test_extracts_basic_ticker(self):
        self.assertEqual(
            ticker_extractor.extract_from_text("$TSLA to the moon"),
            ["TSLA"],
        )

    def test_extracts_multiple_with_repeats(self):
        self.assertEqual(
            ticker_extractor.extract_from_text("$TSLA and $NVDA and $TSLA"),
            ["TSLA", "NVDA", "TSLA"],
        )

    def test_ignores_lowercase(self):
        self.assertEqual(ticker_extractor.extract_from_text("$tsla"), [])

    def test_filter_with_whitelist(self):
        whitelist = {"TSLA", "NVDA"}
        blacklist: set[str] = set()
        self.assertEqual(
            ticker_extractor.filter_tickers(
                ["TSLA", "FAKE", "NVDA"], whitelist, blacklist
            ),
            ["TSLA", "NVDA"],
        )

    def test_blacklist_removes_ticker(self):
        whitelist = {"TSLA", "LOL"}
        blacklist = {"LOL"}
        self.assertEqual(
            ticker_extractor.filter_tickers(["TSLA", "LOL"], whitelist, blacklist),
            ["TSLA"],
        )


if __name__ == "__main__":
    unittest.main()
