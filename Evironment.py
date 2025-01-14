import gym
import cv2


class GymEnvironment:
    def __init__(self):
        self.gym = gym.make('Breakout-v0')
        self.obs = None
        self.terminal = None

        self.screen_width = 84
        self.screen_height = 84

    def render(self):
        self.gym.render()

    def num_actions(self):
        return self.gym.action_space.n

    def restart(self):
        self.obs = self.gym.reset()
        self.obs = None
        self.terminal = None

    def act(self, action):
        self.obs, reward, self.terminal, _ = self.gym.step(action)
        return reward

    def get_screen(self):
        assert self.obs is not None
        return cv2.resize(cv2.cvtColor(self.obs, cv2.COLOR_RGB2GRAY), (self.screen_width, self.screen_height))

    def is_terminal(self):
        assert self.terminal is not None
        return self.terminal
