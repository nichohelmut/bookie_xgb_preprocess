import datetime
from datetime import timezone

import google.auth
import pandas_gbq


def read_bigquery(table_name):
    credentials, project_id = google.auth.default()
    df = pandas_gbq.read_gbq('select * from `footy-323809.statistics.{}`'.format(table_name),
                             project_id=project_id,
                             credentials=credentials,
                             location='europe-west1')

    return df


def write(df, project_id, output_dataset_id, output_table_name, credentials):
    print("write to bigquery")
    df.to_gbq(
        "{}.{}".format(output_dataset_id, output_table_name),
        project_id=project_id,
        if_exists="replace",
        credentials=credentials,
        progress_bar=None
    )
    print("Query complete. The table is updated.")


def predictable_columns():
    return [
        'Pre_Match_PPG__Home_', 'Pre_Match_PPG__Away_', 'attendance', 'home_ppg', 'away_ppg',
        'average_goals_per_match_pre_match', 'btts_percentage_pre_match',
        'over_15_percentage_pre_match', 'over_25_percentage_pre_match',
        'over_35_percentage_pre_match', 'over_45_percentage_pre_match',
        'over_15_HT_FHG_percentage_pre_match',
        'over_05_HT_FHG_percentage_pre_match',
        'average_corners_per_match_pre_match',
        'average_cards_per_match_pre_match', 'odds_ft_home_team_win',
        'odds_ft_draw', 'odds_ft_away_team_win', 'odds_ft_over15',
        'odds_ft_over25', 'odds_ft_over35', 'odds_ft_over45', 'odds_btts_yes',
        'odds_btts_no', 'ht_aa_0', 'ht_aa_1', 'ht_aa_2', 'ht_aa_3', 'ht_aa_4', 'awt_aa_0',
        'awt_aa_1', 'awt_aa_2', 'awt_aa_3', 'awt_aa_4', 'AVGHTGDIFF', 'AVGATGDIFF', 'H_result_1',
        'H_result_2', 'A_result_1', 'A_result_2', 'H_HTGDIFF_1', 'H_HTGDIFF_2',
        'A_ATGDIFF_1', 'A_ATGDIFF_2', 'H_AVGHTGDIFF_1', 'A_AVGATGDIFF_1'
    ]


def row_with_date(df):
    df["row_added"] = datetime.datetime.now(timezone.utc)
    df["row_added"] = df["row_added"].dt.strftime("%Y-%m-%d-%H-%M")
    df["row_added"] = df["row_added"].astype(str)

    return df
