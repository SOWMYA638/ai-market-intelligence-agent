class MarketReport:
    """
    Responsible for formatting market reports.
    """

    @staticmethod
    def print_major_indices(indices_df):
        """
        Prints the major market indices.
        """

        print("=" * 60)
        print("📊 MAJOR INDICES")
        print("=" * 60)

        print(indices_df.to_string(index=False))

        print()

    @staticmethod
    def print_overview(overview, breadth):
        """
        Prints market overview and market breadth.
        """

        print("=" * 60)
        print("📈 MORNING MARKET REPORT")
        print("=" * 60)

        print("\n📊 MARKET OVERVIEW")
        print("-" * 60)

        for key, value in overview.items():
            print(f"{key:<20}: {value}")

        print("\n📈 MARKET BREADTH")
        print("-" * 60)

        for key, value in breadth.items():
            print(f"{key:<20}: {value}")

        print("\n" + "=" * 60)