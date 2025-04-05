class CEnemySpawner:
    def __init__(self, level_data, enemy_data):
        self.spawn_events = level_data["enemy_spawn_events"]  
        self.enemy_types = enemy_data 
        self.elapsed_time = 0  