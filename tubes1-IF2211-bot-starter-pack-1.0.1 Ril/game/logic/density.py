import random
from typing import Optional, List, Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class GreedyDensityBot(BaseLogic):
    """Bot #3: Greedy by Efficiency (Value/Distance) - Pilih diamond dengan rasio nilai/jarak tertinggi"""
    
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        
    def next_move(self, board_bot: GameObject, board: Board):
        try:
            props = board_bot.properties
            current_position = board_bot.position
            
            # Priority 1: If carrying 5 diamonds, return to base
            if props.diamonds >= 5:
                base = props.base
                if base:
                    move = self.move_to_goal(current_position, base)
                    if move != (0, 0):
                        return move
            
            # Priority 2: Find most efficient diamond (GREEDY BY VALUE/DISTANCE)
            diamonds = self.get_diamonds(board)
            if diamonds:
                best_diamond = self.find_most_efficient_diamond(current_position, diamonds)
                if best_diamond:
                    move = self.move_to_goal(current_position, best_diamond.position)
                    if move != (0, 0):
                        return move
            
            # Priority 3: Return to base if carrying diamonds
            if props.diamonds > 0:
                base = props.base
                if base:
                    move = self.move_to_goal(current_position, base)
                    if move != (0, 0):
                        return move
            
            # Priority 4: Random exploration
            return self.get_random_move()
            
        except Exception as e:
            print(f"Error in GreedyEfficiencyBot: {e}")
            return self.get_random_move()
    
    def find_most_efficient_diamond(self, current_pos: Position, diamonds: List[GameObject]) -> Optional[GameObject]:
        """GREEDY STRATEGY: Pilih diamond dengan efisiensi tertinggi (value/distance)"""
        if not diamonds:
            return None
            
        best_diamond = None
        max_efficiency = 0
        
        for diamond in diamonds:
            try:
                distance = self.manhattan_distance(current_pos, diamond.position)
                value = self.get_diamond_value(diamond)
                
                # Calculate efficiency: value / distance
                # Add 1 to distance to avoid division by zero
                efficiency = value / (distance + 1)
                
                if efficiency > max_efficiency:
                    max_efficiency = efficiency
                    best_diamond = diamond
                    
            except Exception:
                continue
                
        return best_diamond
    
    def get_diamond_value(self, diamond: GameObject) -> int:
        """Get diamond value/points"""
        try:
            # Try to get value from properties
            if hasattr(diamond, 'properties'):
                if hasattr(diamond.properties, 'value'):
                    return diamond.properties.value
                elif hasattr(diamond.properties, 'points'):
                    return diamond.properties.points
            
            # Fallback: assume red diamonds (DiamondGameObject) = 2, blue = 1
            if hasattr(diamond, 'type') and diamond.type == "DiamondGameObject":
                return 2  # Red diamond
            else:
                return 1  # Blue diamond
                
        except:
            return 1  # Default value
    
    def get_diamonds(self, board: Board) -> List[GameObject]:
        """Get all diamonds on the board"""
        diamonds = []
        try:
            for game_object in board.game_objects:
                if hasattr(game_object, 'type') and game_object.type == "DiamondGameObject":
                    diamonds.append(game_object)
                elif "Diamond" in str(type(game_object)):
                    diamonds.append(game_object)
        except:
            pass
        return diamonds
    
    def manhattan_distance(self, pos1: Position, pos2: Position) -> int:
        """Calculate Manhattan distance between two positions"""
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
    
    def move_to_goal(self, current_pos: Position, goal_pos: Position) -> Tuple[int, int]:
        """Move towards goal position"""
        try:
            delta_x, delta_y = get_direction(
                current_pos.x, current_pos.y,
                goal_pos.x, goal_pos.y
            )
            
            # Prevent invalid move (0, 0)
            if delta_x == 0 and delta_y == 0:
                return self.get_random_move()
                
            return delta_x, delta_y
        except:
            return self.get_random_move()
    
    def get_random_move(self) -> Tuple[int, int]:
        """Get a random valid move"""
        return random.choice(self.directions)