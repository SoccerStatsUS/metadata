

# presume a 5 x 5 grid to start




positions = {
    'LB' : ('left back', (0, 0)
    'LWB': 'left wing back', (0,
    'RB' : 'right back',
    'RWB': 'right wing back',    

    'SW': 'sweeper',
    'CB': 'center back',

    'DM': 'defensive midfielder',
    'CM': 'central midfielder',
    'AM': 'attacking midfielder',
    
    'LM': 'left midfielder',
    'RM': 'right midfielder',

    'WF': 'withdrawn forward',
    'IF': 'inside forward',
    'LIF': 'left inside forward',
    'RIF': 'right inside forward',    

    'CF': 'centre forward',
    'LF': 'left forward',
    'RF': 'right forward',    

    'LW': 'left wing',
    'RW': 'right wing',
}


Subformations: {


    '2-3-5': [
        ],    

    '3-4-3': [
        ],

    '3-5-2': [
        '3-1-4-2',
        '3-4-1-2',
        '3-5-1-1',
        ],

    '3-6-1': [
        '3-2-2-2-2',
        ],    
    
    '4-4-2': [
        '4-1-2-1-2',
        '4-1-3-2',
        '4-2-2-2',        
        '4-4-1-1',
        ],
    
    '4-3-3': [
        '4-1-2-3',
        ],
    
    '4-5-1': [
        '4-3-2-1',
        '4-2-3-1',                
        '4-1-4-1',
        ],
    
    '5-3-2': [
        ],

    '5-4-1': [
        ],    
    
    }
              


map = [

    ('2-3-5', ['CB', 'CB', 'LM', 'CM', 'RM', 'LW', 'LIF', 'CF', 'RIF', 'RW']),
    ('2-3-2-3', ['CB', 'CB', 'LWB', 'DM', 'RWB', 'AM', 'AM', 'LW', 'CF', 'RW']),
    ('3-2-2-3', ['CB', 'CB', 'CB', 'DM', 'DM', 'AM', 'AM', 'LW', 'CF', 'RW']), #WM
    # ('3-2-3-2', ['CB', 'CB', 'CB', 'DM', 'DM', 'AM', 'AM', 'LW', 'CF', 'RW']), #WW


    # 3-3-4

    ('3-3-4' []),

    ### 3-4-3
    
    ('3-4-3', ['CB', 'CB', 'CB', 'LM', 'CM', 'CM', 'RM', 'LW', 'CF', 'RW']),

    ### 3-5-2
    ('3-5-2', ['CB', 'SW', 'CB', 'LWB', 'CM', 'CM', 'CM', 'RWB', 'LF', 'RF']),

    ('3-5-1-1', ['CB', 'SW', 'CB', 'LWB', 'CM', 'CM', 'CM', 'RWB', 'WF', 'CF']),    
    ('3-4-1-2', ['CB', 'SW', 'CB', 'LWB', 'CM', 'CM', 'RWB', 'AM', 'LF', 'RF']),        


    ### 4-2-4

    ('4-2-4', ['LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'LW', 'LF', 'RF', 'RW']),


    ### 4-3-3

    ('4-3-3', ['LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CM', 'LW', 'CF', 'RW']),


    ### 4-4-2

    ('4-4-2', ['LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'LF', 'RF']),
    ('4-4-1-1', ['LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'WF', 'CF']),
    ('4-2-2-2', ['LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'LF', 'RF']),    
    ('4-1-2-1-2', ['LB', 'CB', 'CB', 'RB', 'DM', 'LM', 'RM', 'AM', 'RF', 'LF']),
    ('4-1-2-3', ['LB', 'CB', 'CB', 'RB', 'DM', 'CM', 'CM', 'LW', 'CF', 'RW']),


    ### 4-5-1

    ('4-5-1', ['LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'AM', 'CF']),
    ('4-1-4-1', ['LB', 'CB', 'CB', 'RB', 'DM', 'LM', 'CM', 'CM', 'RM', 'CF']),
    ('4-2-3-1', ['LB', 'CB', 'CB', 'RB', 'Dm', 'DM', 'LM', 'AM', 'RF', 'CF']),
    ('4-1-3-2': ['LB', 'CB', 'CB', 'RB', 'DM', 'LM', 'CM', 'RM', 'LF', 'RF']),
    ('4-3-2-1', ['LB', 'CB', 'CB', 'RB', 'LM', 'DM', 'RM', 'AM', 'AM', 'CF']),

    ### 5-3-2

    ('5-3-2', ['LWB', 'CB', 'SW', 'CB', 'RWB', 'CM', 'CM', 'CM', 'LF', 'RF']),


    ### 5-4-1
    
    ('5-4-1', ['LWB', 'CB', 'SW', 'CB', 'RWB', 'LM', 'CM', 'CM', 'RM', 'CF']),        

]
