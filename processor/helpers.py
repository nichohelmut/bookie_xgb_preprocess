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
        'Pre_Match_PPG__Home_', 'Pre_Match_PPG__Away_', 'attendance',
        'average_goals_per_match_pre_match', 'btts_percentage_pre_match',
        'over_15_percentage_pre_match', 'over_25_percentage_pre_match',
        'over_35_percentage_pre_match', 'over_45_percentage_pre_match',
        'over_15_HT_FHG_percentage_pre_match', 'over_05_HT_FHG_percentage_pre_match',
        'average_corners_per_match_pre_match', 'average_cards_per_match_pre_match', 'ht_aa_0', 'ht_aa_1', 'ht_aa_2',
        'ht_aa_3', 'ht_aa_4', 'awt_aa_0',
        'awt_aa_1', 'awt_aa_2', 'awt_aa_3', 'awt_aa_4', 'AVGHTGDIFF', 'AVGATGDIFF', 'H_result_1',
        'H_result_2', 'A_result_1', 'A_result_2', 'H_HTGDIFF_1', 'H_HTGDIFF_2',
        'A_ATGDIFF_1', 'A_ATGDIFF_2', 'H_AVGHTGDIFF_1', 'A_AVGATGDIFF_1'
    ]


def row_with_date(df):
    df["row_added"] = datetime.datetime.now(timezone.utc)
    df["row_added"] = df["row_added"].dt.strftime("%Y-%m-%d-%H-%M")
    df["row_added"] = df["row_added"].astype(str)

    return df


# availiable columns for later consideration
# ['attendance', 'Pre_Match_PPG__Home_', 'Pre_Match_PPG__Away_',
#        'home_ppg', 'away_ppg', 'total_goal_count', 'total_goals_at_half_time',
#        'home_team_goal_count_half_time', 'away_team_goal_count_half_time',
#        'home_team_corner_count', 'away_team_corner_count',
#        'home_team_yellow_cards', 'home_team_red_cards',
#        'away_team_yellow_cards', 'away_team_red_cards', 'home_team_shots',
#        'away_team_shots', 'home_team_shots_on_target',
#        'away_team_shots_on_target', 'home_team_shots_off_target',
#        'away_team_shots_off_target', 'home_team_fouls', 'away_team_fouls',
#        'home_team_possession', 'away_team_possession',
#        'average_goals_per_match_pre_match', 'btts_percentage_pre_match',
#        'over_15_percentage_pre_match', 'over_25_percentage_pre_match',
#        'over_35_percentage_pre_match', 'over_45_percentage_pre_match',
#        'over_15_HT_FHG_percentage_pre_match',
#        'over_05_HT_FHG_percentage_pre_match',
#        'average_corners_per_match_pre_match',
#        'average_cards_per_match_pre_match', 'odds_ft_home_team_win',
#        'odds_ft_draw', 'odds_ft_away_team_win', 'odds_ft_over15',
#        'odds_ft_over25', 'odds_ft_over35', 'odds_ft_over45', 'odds_btts_yes',
#        'odds_btts_no', 'home_team_first_half_cards',
#        'home_team_second_half_cards', 'away_team_first_half_cards',
#        'away_team_second_half_cards', 'team_a_xg', 'team_b_xg', 'Game_Week',
#        'over_15_2HG_percentage_pre_match', 'over_05_2HG_percentage_pre_match',
#        'ht_aa_0', 'ht_aa_1', 'ht_aa_2', 'ht_aa_3', 'ht_aa_4', 'awt_aa_0',
#        'awt_aa_1', 'awt_aa_2', 'awt_aa_3', 'awt_aa_4', 'HTGDIFF', 'ATGDIFF',
#        'AVGHTGDIFF', 'AVGATGDIFF', 'H_result_1', 'H_result_2', 'A_result_1',
#        'A_result_2', 'H_HTGDIFF_1', 'H_HTGDIFF_2', 'A_ATGDIFF_1',
#        'A_ATGDIFF_2', 'H_AVGHTGDIFF_1', 'A_AVGATGDIFF_1']