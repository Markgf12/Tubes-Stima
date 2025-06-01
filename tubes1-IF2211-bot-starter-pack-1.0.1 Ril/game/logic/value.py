import random
from typing import Optional, List, Tuple
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class GreedyValueBot(BaseLogic):
    """Bot #2: Greedy by Highest Value - Selalu kejar diamond dengan nilai tertinggi"""
    
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
            
            # Priority 2: Find highest value diamond (GREEDY BY VALUE)
            diamonds = self.get_diamonds(board)
            if diamonds:
                best_diamond = self.find_highest_value_diamond(diamonds)
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
            print(f"Error in GreedyValueBot: {e}")
            return self.get_random_move()
    
    def find_highest_value_diamond(self, diamonds: List[GameObject]) -> Optional[GameObject]:
        """GREEDY STRATEGY: Pilih diamond dengan nilai tertinggi"""
        if not diamonds:
            return None
            
        best_diamond = None
        max_value = 0
        
        for diamond in diamonds:
            try:
                # Get diamond value/points
                value = self.get_diamond_value(diamond)
                
                if value > max_value:
                    max_value = value
                    best_diamond = diamond
                    
            except Exception:
                continue
        
        # If no diamond with specific value found, return any diamond
        return best_diamond if best_diamond else diamonds[0] if diamonds else None
    
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