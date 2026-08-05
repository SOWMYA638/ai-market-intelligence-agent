import pandas as pd


class IndexAnalytics:
    """
    Performs analytics related to Indian market indices.
    """

    MAJOR_INDICES = [
        "NIFTY 50",
        "NIFTY BANK",
        "NIFTY FINANCIAL SERVICES",
        "NIFTY MIDCAP 100",
        "NIFTY SMALLCAP 100",
        "INDIA VIX"
    ]

    REQUIRED_COLUMNS = [
        "index",
        "last",
        "variation",
        "percentChange"
    ]

    def get_major_indices(self, indices_df: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a filtered DataFrame containing only the
        major Indian market indices.

        Parameters
        ----------
        indices_df : pd.DataFrame
            Complete indices DataFrame from NSE.

        Returns
        -------
        pd.DataFrame
            Filtered DataFrame containing only major indices.
        """

        if indices_df.empty:
            return pd.DataFrame(columns=self.REQUIRED_COLUMNS)

        major_indices = indices_df[
            indices_df["index"].isin(self.MAJOR_INDICES)
        ]

        major_indices = major_indices[self.REQUIRED_COLUMNS]

        major_indices = major_indices.reset_index(drop=True)

        return major_indices