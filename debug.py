import world
import event
a = world.TheWorld(None, (3, 3, 3))
u, o_id= a.control_add_user()
a.api_action(u,o_id,(0,0,2),event.EVENT_ACTION_MOVE)
a.control_start_game()