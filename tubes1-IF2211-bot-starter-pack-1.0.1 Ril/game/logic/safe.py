# File: game/logic/greedy_safe_bot.py

import random
from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position

class GreedySafeBot(BaseLogic):
    """Bot #4: Greedy by (Value × Safety) / Distance"""
    
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        
    def next_move(self, board_bot: GameObject, board: Board):
        """Main bot logic with safety considerations"""
        try:
            props = board_bot.properties
            current_position = board_bot.position
            
            # Priority 1: If carrying 5 diamonds, return to base
            if props.diamonds >= 5:
                base = props.base
                if base:
                    delta_x, delta_y = self.get_direction_to_target(current_position, base)
                    return delta_x, delta_y
            
            # Priority 2: Find best diamond with safety factor
            best_diamond = self.find_best_safe_diamond(current_position, board)
            if best_diamond:
                delta_x, delta_y = self.get_direction_to_target(current_position, best_diamond.position)
                return delta_x, delta_y
            
            # Priority 3: If carrying diamonds, return to base
            if props.diamonds > 0:
                base = props.base
                if base:
                    delta_x, delta_y = self.get_direction_to_target(current_position, base)
                    return delta_x, delta_y
            
            # Priority 4: Safe exploration
            return self.safe_move(current_position, board)
            
        except Exception as e:
            # Fallback to random move if any error
            return random.choice(self.directions)
    
    def find_best_safe_diamond(self, current_pos: Position, board: Board):
        """Find diamond with best (value × safety) / distance score"""
        diamonds = self.get_all_diamonds(board)
        enemies = self.get_enemy_bots(board)
        
        if not diamonds:
            return None
        
        best_diamond = None
        best_score = 0
        
        for diamond in diamonds:
            try:
                # Calculate distance (Manhattan)
                distance = abs(current_pos.x - diamond.position.x) + abs(current_pos.y - diamond.position.y)
                if distance == 0:
                    distance = 1  # Avoid division by zero
                
                # Get diamond value
                value = self.get_diamond_value(diamond)
                
                # Calculate safety factor
                safety = self.calculate_safety(diamond.position, enemies)
                
                # Calculate score: (value × safety) / distance
                score = (value * safety) / distance
                
                if score > best_score:
                    best_score = score
                    best_diamond = diamond
                    
            except:
                continue
        
        return best_diamond
    
    def calculate_safety(self, target_pos: Position, enemies):
        """Calculate safety factor: min(1.0, max(0.1, min_enemy_distance / 10.0))"""
        if not enemies:
            return 1.0  # Maximum safety if no enemies
        
        min_distance = 999
        for enemy in enemies:
            try:
                distance = abs(target_pos.x - enemy.position.x) + abs(target_pos.y - enemy.position.y)
                min_distance = min(min_distance, distance)
            except:
                continue
        
        # Safety formula as specified
        return min(1.0, max(0.1, min_distance / 10.0))
    
    def safe_move(self, current_pos: Position, board: Board):
        """Move to safest direction"""
        enemies = self.get_enemy_bots(board)
        
        best_direction = None
        best_safety = -1
        
        for direction in self.directions:
            new_x = current_pos.x + direction[0]
            new_y = current_pos.y + direction[1]
            new_pos = Position(new_x, new_y)
            
            safety = self.calculate_safety(new_pos, enemies)
            if safety > best_safety:
                best_safety = safety
                best_direction = direction
        
        return best_direction if best_direction else random.choice(self.directions)
    
    def get_all_diamonds(self, board: Board):
        """Get all diamonds from board"""
        diamonds = []
        try:
            for obj in board.game_objects:
                if hasattr(obj, 'type') and 'Diamond' in str(obj.type):
                    diamonds.append(obj)
        except:
            pass
        return diamonds
    
    def get_enemy_bots(self, board: Board):
        """Get all enemy bots"""
        enemies = []
        try:
            for obj in board.game_objects:
                if hasattr(obj, 'type') and 'Bot' in str(obj.type):
                    enemies.append(obj)
        except:
            pass
        return enemies
    
    def get_diamond_value(self, diamond):
        """Get diamond value (red=2, blue=1)"""
        try:
            if hasattr(diamond, 'properties') and hasattr(diamond.properties, 'points'):
                return diamond.properties.points
            elif 'Red' in str(diamond.type):
                return 2
            else:
                return 1
        except:
            return 1
    
    def get_direction_to_target(self, current_pos: Position, target_pos: Position):
        """Get direction to move towards target"""
        try:
            if current_pos.x < target_pos.x:
                return (1, 0)
            elif current_pos.x > target_pos.x:
                return (-1, 0)
            elif current_pos.y < target_pos.y:
                return (0, 1)
            elif current_pos.y > target_pos.y:
                return (0, -1)
            else:
                return random.choice(self.directions)
        except:
            return random.choice(self.directions)