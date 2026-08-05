from src.services.analytics_service import AnalyticsService
from src.reports.market_report import MarketReport


def main():
    analytics = AnalyticsService()

    # Fetch data
    major_indices = analytics.get_major_indices()
    overview = analytics.market_overview()
    breadth = analytics.market_breadth()

    # Print report
    MarketReport.print_major_indices(major_indices)
    MarketReport.print_overview(overview, breadth)


if __name__ == "__main__":
    main()