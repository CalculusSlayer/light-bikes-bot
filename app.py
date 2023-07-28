import player
import time


def main():
    game = player.Game()
    # game_id = game.create(4).json()['id']
    game_id = 1121
    # print(game_id)
    game_json = game.joinGame(game_id, "nayeeeeeeeel").json()
    current_player = game_json[0]["current_player"]

    player_id = current_player["id"]
    x = current_player["x"]
    y = current_player["y"]

    # board_len = len()
    if x > 11:
        i = -1
    else:
        i = 1

    while True:
        print(x, y)
        x += i
        current_move = game.move(game_id, player_id, x, y)

        if int(current_move.status_code) >= 400:
            break
        time.sleep(0.1)

    


if __name__ == '__main__':
    main()
