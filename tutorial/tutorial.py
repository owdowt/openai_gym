"""
Written VSCode Jupyter Format
"""

#%%
import gym

#%%
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())  # take a random action
env.close()

#%%
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()  # 環境をリセットすると最初の状態に戻る（棒が中心に戻る）
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

#%%
