import time


def game():
    """玩游5秒钟
    """
    for i in range(5):
        print("---正在玩游戏---")
        time.sleep(1)


def shopping():
    """逛街5秒
    """
    for i in range(5):
        print("---正在逛街---")
        time.sleep(1)


def main():
    shopping()
    game()
