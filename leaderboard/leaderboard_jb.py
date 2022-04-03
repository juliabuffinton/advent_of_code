import os
import datetime as dt
import requests
from datetime import datetime

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import random


def build_cookie(file):
    keys = ['_ga','session','_gid','_gat']
    cookie = ''

    with open(file) as f:
        for l in f:
            l = l.replace('\n','')
            l = l.split('\t')
            if any(x in l for x in keys):
                cookie += l[-2] + '=' + l[-1] + '; '

    return cookie[:-2]


def get_data(id_number: int, cookie: str, year: int = 2020):
    """Retrieves AoC Leaderboard data as JSON (i.e., Dict)

    Args:
        id_number: int - identification number for leaderboard info;
            viewable in the URL for downloading the info manually
        year: int - year for which to retrieve info
        cookie: str - cookie information with which to retrieve info;
            viewable in developer tools upon download (~1 month expiration)

    Returns:
        AoC Leaderboard information as JSON

    ```
    import leaderboard
    aoc_leaderboard_info = leaderboard.get_data(1524967)
    ```
    """
    result = requests.get(
        f'https://adventofcode.com/{year}/leaderboard/private/view/{id_number}.json',
        headers={'cookie': cookie},
    )
    return result.json()


def parse_json(data, contestants):
    """parse the AoC leaderboard data into a dataframe with one row per participant
    data: leaderboard data from JSON file
    contestants: dataframe with contestant names and AoC display names
    returns: df dataframe with one row per contestant and submission times per problem/part"""

    df = pd.DataFrame()

    for m in data['members'].keys():
        name = data['members'][m]['name']
        name = m if name is None else name
        if name in contestants['AoC Display name'].values:
            print_name = contestants[contestants['AoC Display name'] == name].Name.values[0]
            times = {'Contestant': print_name, 'score': int(data['members'][m]['local_score']),
                     'stars': int(data['members'][m]['stars'])}
            for day in data['members'][m]['completion_day_level'].keys():
                for p in data['members'][m]['completion_day_level'][day].keys():
                    times[day + '_' + p + '_time'] = dt.datetime.fromtimestamp(
                        data['members'][m]['completion_day_level'][day][p]['get_star_ts'])

            df = df.append(times, ignore_index=True)

    for col in df.columns:
        if col in ['score', 'stars']:
            df[col] = df[col].astype(int)
        elif col == 'Contestant':
            pass
        else:
            problem = col.replace('time', 'rank')
            df[problem] = df[col].rank()

    df.sort_values(by='Contestant', inplace=True)
    df.reset_index(inplace=True, drop=True)

    return df


def raffle_tickets(problems, deadline, ticketsPerPart=1):
    """get the number of raffle tickets per contestant
    problems: list of integer problem numbers
    deadline: datetime deadline for submitting the problems in order to be considered
    ticketsPerPart: int or list of ints with the nubmer of tickets reveived for completing each part of each problem
    return: DataFrame with the number of tickets for each contestant"""

    # get the time columns for all of the given problems
    # assumes there are 2 parts per problem
    cols = [str(int(p)) + '_1_time' for p in problems] + [str(int(p)) + '_2_time' for p in problems]
    cols = [col for col in results if col in cols]

    # check the times to get the number of tickets per contestant 
    tickets = (results[cols] <= deadline) * ticketsPerPart
    score = pd.DataFrame(results.Contestant)
    score['Raffle Tickets'] = tickets.sum(axis=1)

    return score


def plot():

    # weekly raffel trace
    problems = [deadlines.Problem[args.week - 1]]
    deadline = deadlines.Deadline[args.week - 1]
    tickets = raffle_tickets(problems, deadline)
    title1 = '<b>Week {w} Raffle Entries<b>'.format(w=args.week)
    trace1 = go.Bar(x=tickets['Contestant'],
                    y=tickets['Raffle Tickets'])

    # Final Raffle
    problems = deadlines.Problem[:args.week]
    deadline = deadlines.Deadline.max()
    tickets = raffle_tickets(problems, deadline)
    title2 = '<b>Final Raffle Entries<b>'
    trace2 = go.Bar(x=tickets['Contestant'],
                    y=tickets['Raffle Tickets'])

    # build subplots
    fig = make_subplots(rows=2, cols=1,subplot_titles=(title1,title2))
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 2, 1)

    # set each y-axis to nonnegative integer ticks
    for ax in fig['layout']:
        if ax[:5]=='yaxis':
            fig['layout'][ax]['dtick']=1
            fig['layout'][ax]['rangemode']='nonnegative'
            
    fig.update_layout(showlegend=False,title='<b>LMI Coding Challenge Leaderboard<b>')
    fig.update_layout(
        autosize=False,
        width=900,
        height=800)
    fig.update_xaxes(tickangle=90)

    #fig.show()

    date = datetime.today().strftime('%d%m%Y')
    fig.write_image('images/leaderboard_' + str(args.week) + '_' + date + '.png')

    return

def raffle_drawing(raffle_type,previous_winners):

    if raffle_type == 'week':
        problems = [deadlines.Problem[args.week - 1]]
        deadline = deadlines.Deadline[args.week - 1]
        tickets = raffle_tickets(problems, deadline)
    elif raffle_type == 'final':
        problems = deadlines.Problem[:args.week]
        deadline = deadlines.Deadline.max()
        tickets = raffle_tickets(problems, deadline)
    else:
        return

    entries = []
    for idx,row in tickets.iterrows():
        if row['Raffle Tickets'] > 0:
            if (raffle_type == 'final') or (row.Contestant not in previous_winners.Winner.values):
                entries += [row.Contestant] * row['Raffle Tickets']
    
    print('Raffle Winner: {x}'.format(x = random.choice(entries)))
    return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_dir', default=os.curdir, type=str, help=f'''''')
    parser.add_argument('--week', default=1, type=int, help=f'''''')
    parser.add_argument('--AOCyear', default=2020, type=int)
    parser.add_argument('--leaderboard', default=1542191, type=int)
    parser.add_argument('--drawing',type=str)

    args = parser.parse_args()

    # get cookie
    cookie = build_cookie('adventofcode.com_cookies-jb.txt')

    # read in leaderboard data
    data = get_data(args.leaderboard,cookie,args.AOCyear)

    # read in contestant data
    file = r'Contestants.xlsx'
    contestants = pd.read_excel(os.path.join(args.input_dir, file),dtype=str)

    # read in deadline data
    file = r'deadlines.xlsx'
    deadlines = pd.read_excel(os.path.join(args.input_dir, file))

    # read in past winners
    file = r'winners.xlsx'
    winners = pd.read_excel(os.path.join(args.input_dir,file))

    # parse AoC data
    results = parse_json(data, contestants)

    # plot and display
    plot()

    # raffle drawing
    raffle_drawing(args.drawing,winners)




 



