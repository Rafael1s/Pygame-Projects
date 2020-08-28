
from base_apple_snake import Base, Apple, Snake
'''
 Breadth First Search
 The breadth first search is used by the path solver to find the shortest path along the map.
'''

''' Generates the shortest path from the snake’s head to the apple using BFS algorithm.'''

class Player(Base):
    def __init__(self, snake: Snake, apple: Apple, **kwargs):
        """
        :param snake: Snake instance
        :param apple: Apple instance
        """
        super().__init__(**kwargs)
        self.snake = snake
        self.apple = apple

    def _get_neighbors(self, node):
        """
        fetch and yield the four neighbours of a node
        :param node: (node_x, node_y)
        """
        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            yield self.node_add(node, diff)

    @staticmethod
    def is_node_in_queue(node: tuple, queue: iter):
        """
        Check if element is in a nested list
        """
        return any(node in sublist for sublist in queue)

    def is_invalid_move(self, node: tuple, snake: Snake):
        """
        Similar to dead_checking, this method checks if a given node is a valid move
        :return: Boolean
        """
        x, y = node
        if not 0 <= x < self.cell_width or not 0 <= y < self.cell_height or node in snake.body:
            return True
        return False

class BFS(Player):
    def __init__(self, snake: Snake, apple: Apple, **kwargs):
        """
        :param snake: Snake instance
        :param apple: Apple instance
        """
        super().__init__(snake=snake, apple=apple, **kwargs)

    def run_bfs(self):
        """
        Run BFS searching and return the full path of best way to apple from BFS searching
        """
        
        ''' internal list = path, queue = list of paths '''
        queue = [[self.snake.get_head()]]

        while queue:
            path = queue[0]
            future_head = path[-1]
            
            ## print('run_bfs: path: ', path)

            # If snake eats the apple, return the next move after snake's head
            if future_head == self.apple.location:
                return path

            for next_node in self._get_neighbors(future_head):
                if (
                    self.is_invalid_move(node=next_node, snake=self.snake)
                    or self.is_node_in_queue(node=next_node, queue=queue)
                ):
                    continue
                new_path = list(path)
                new_path.append(next_node)
                queue.append(new_path)

            queue.pop(0)

    def next_node(self):
        """
        Run the BFS searching and return the next move in this path
        """
        path = self.run_bfs()
        return path[1]
    
class Mixed(Player):
    def __init__(self, snake: Snake, apple: Apple, **kwargs):
        """
        :param snake: Snake instance
        :param apple: Apple instance
        """
        super().__init__(snake=snake, apple=apple, **kwargs)
        self.kwargs = kwargs
        
        self.GO_APPLE  = -12
        self.GO_TAIL  = -13
        

    def escape(self):
        head = self.snake.get_head()
        largest_neibhour_apple_distance = 0
        newhead = None
        go_to_smth = -1
        ## count = 0        
        ## length = len(self.snake.body)
        ## debug_len = 187
        
        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neibhour = self.node_add(head, diff)
            
            ## count += 1
            
            if self.snake.dead_checking(head=neibhour, check=True):
                ## if length > debug_len:
                ##   print('escape: path is Dead: ', count)                
                continue

            ''' Manhattan distance: |x1 - x2| + |y1 - y2| '''
            neibhour_apple_distance = (
                abs(neibhour[0] - self.apple.location[0]) + abs(neibhour[1] - self.apple.location[1])
            )
            # Find the neibhour which has greatest Manhattan distance to apple and has path to tail
            
            if largest_neibhour_apple_distance < neibhour_apple_distance:
                snake_tail = Apple()
                snake_tail.location = self.snake.body[1]
                # Create a virtual snake with a neibhour as head, to see if it has a way to its tail,
                # thus remove two nodes from body: one for moving one step forward, one for avoiding dead checking
                snake = Snake(body=self.snake.body[2:] + [neibhour])
                bfs = BFS(snake=snake, apple=snake_tail, **self.kwargs)
                bfs_path = bfs.run_bfs()
                if bfs_path is None:
                    ## if length > debug_len:
                    ##     print('escape: path is None: ', count)
                    continue
                largest_neibhour_apple_distance = neibhour_apple_distance
                newhead = neibhour
                ## if length > debug_len:
                ##     print('escape: path is Fixed: ', count, 'newhead: ', newhead)
                go_to_smth = self.GO_TAIL
                #print('escape: path (GO_TAIL): ')
        
        return newhead, bfs_path, go_to_smth

    def run_mixed(self):
        """
        Mixed strategy
        """
        bfs = BFS(snake=self.snake, apple=self.apple, **self.kwargs)

        bfs_path = bfs.run_bfs()
        

        # If the snake does not have the path to apple, try to follow its tail to escape
        if bfs_path is None:
            ## print('run_mixed: bfs path is None')
            return self.escape()
        
        # Send a virtual snake to see when it reaches the apple, does it still have a path to its own tail, to keep it
        # alive
        length = len(self.snake.body)
        
        virtual_snake_body = (self.snake.body + bfs_path[1:])[-length:]
        #print('snake.body: ', self.snake.body, ', path[1:] : ', path[1:])
        #print('virtual_snake_body: ', virtual_snake_body)

        virtual_snake_tail = Apple()
        virtual_snake_tail.location = (self.snake.body + bfs_path[1:])[-length - 1]
        virtual_snake = Snake(body=virtual_snake_body)
 
        virtual_snake_longest = BFS(snake=virtual_snake, apple=virtual_snake_tail, **self.kwargs)        
        virtual_snake_longest_path = virtual_snake_longest.run_bfs()

        
        if virtual_snake_longest_path is None:
            ## print('run_mixed: virtual_snake_longest_path is None')
            return self.escape()
        else:
            ## print('run_mixed: head: ', path[1])
            #print('run_mixed: (GO_APPLE): ')
            return bfs_path[1], bfs_path, self.GO_APPLE
        
    

