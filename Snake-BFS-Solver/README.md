This is the Snake that needs to eat an apple on each cell, and there are 196 such cells.    
The apple is shown in red, the head of the snake in green and her tail in blue.    
In this video, the Artificial Snake reaches its maximum possible length = 196.   
In the lower left window, for each step, we see the path that the Snake must go to reach the goal:    
the apple or the tail of the Snake. The tail is selected only if there is no safe path to the apple.   
Algorithm corrects its decision on each step.    

The BFS (Breadth First Search) solver makes the snake to eat the apple along the shortest path     
if it thinks that particular path will be safe for the snake. Otherwise, it makes the snake    
to move until it finds a safe path, in particular, the solver looks for a path to the snake's tail  
and tries to change the path to the apple each step.   


![](images/len_34_t_075.png) ![](images/len_65_t_075.png)    
![](images/len_87_t_075.png) ![](images/len196_t_075.png)


### Snake with Deep-Q-Network

For the Snake trained with Deep Reinforcement Learning algorithm DQN see [here](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Snake-Pygame-DQN).

### References

[AI -Snake game design using Machine Learning](https://www.pantechsolutions.net/ai-snake-game-design-using-machine-learning)     
[Playing Snake with AI](https://mc.ai/playing-snake-with-ai/)     
[Automated Snake Game Solvers via AI Search Algorithms](https://www.semanticscholar.org/paper/Automated-Snake-Game-Solvers-via-AI-Search-Kong-Mayans/ac6b04c7f7a9a3b8f58d7bc3c2ced39fd2c4ac98)    
[Solving the Classic Game of Snake with AI](https://towardsdatascience.com/slitherin-solving-the-classic-game-of-snake-with-ai-part-1-domain-specific-solvers-d1f5a5ccd635)   
[Hamiltonian Cycle: Simple Definition and Example](https://www.statisticshowto.com/hamiltonian-cycle/)     
[Euler and Hamiltonian Paths and Circuits](https://www.youtube.com/watch?v=AwsMTEl79wI)    
[The UNKILLABLE Snake AI (Entire 30x30 game)](https://www.youtube.com/watch?v=YqL7bl3I5IE)     

### Video
See video [Artificial snake on the way](https://www.youtube.com/watch?v=-jNfUrVniNg&t=2s) on youtube.

### Credit
The code is based on Guangyang Li's code https://github.com/DC-Data/SnakeSolver/blob/master/snake.py
