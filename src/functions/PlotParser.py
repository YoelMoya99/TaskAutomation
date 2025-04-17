from argparse import ArgumentParser

def comma_separated(value):
    return [float(item) for item in value.split(',')]

def create_parser():

    # Arg parser set up
    # ------------------------------------------------------------------------
    parser = ArgumentParser(
        description="General command line argument initializer.",
        epilog="for now only works for one script."
        )

    subparsers = parser.add_subparsers(
        dest='command',
        help='Available commands'
        )

    # First command definition with respective flags.
    # ------------------------------------------------------------------------
    command1_parser = subparsers.add_parser(
        'data',
        help='Handles the data range, color and specific values'
        )

    command1_group = command1_parser.add_mutually_exclusive_group(
        required=True
        )

    command1_group.add_argument(
        '--xaxis',
        type=str,
        help='Name of the dataframe column for the x axis'
        )

    command1_group.add_argument(
        '--yaxis',
        type=str,
        help='name of the df column for a y axis'
        )

    command1_group.add_argument(
        '--xrange',
        type=comma_separated,
        help='Pass a comma separated range of values like 1.23,3.21'
        )

    command1_group.add_argument(
        '--yrange',
        type=comma_separated,
        help='Pass a comma separated range of values like 1.23,3.21'
        )

    command1_group.add_argument(
        '--src',
        help='Pass the path with the file that contains the values to plot'
        )

    command1_group.add_argument(
        '--color',
        type=str,
        help='input the color that uses the selected column'
        )

    command1_group.add_argument(
        '--show',
        action='store_true',
        help='it displays all the configurable values and data'
        )

    # Second command definition with respective flags.
    # ------------------------------------------------------------------------
    command2_parser = subparsers.add_parser(
        'format', 
        help='Format of the final plot'
        )
    
    command2_group = command2_parser.add_mutually_exclusive_group(
        required=True
        )
    command2_group.add_argument(
        '--txtsize',
        help="Points of the letter and axis numbers"
        )
    command2_group.add_argument(
        '--width',
        help="Width in inches of the figure"
        )
    command2_group.add_argument(
        '--title',
        help="LaTeX compatible title of the plot"
        )
    command2_group.add_argument(
        '--xlabel',
        help="LaTeX compatible x axis label of the plot"
        )
    command2_group.add_argument(
        '--ylabel',
        help="LaTeX compatible y axis label of the plot"
        )
 
    # Third command definition with respective flags.
    # ------------------------------------------------------------------------
    command3_parser = subparsers.add_parser(
        'build', 
        help='Generates the template for the config file or the plot'
        )
    
    command3_group = command3_parser.add_mutually_exclusive_group(
        required=True
        )
    command3_group.add_argument(
        '--config_template',
        help="Generates the config file with default values"
        )
    command3_group.add_argument(
        '--pdf',
        help="Generates the pdf file with default values"
        )
 
    # Return Namespace with the parsed args.
    # ------------------------------------------------------------------------


    return parser.parse_args()



