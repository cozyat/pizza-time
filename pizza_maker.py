from sprite_creator import get_sprites, bake_timer # type: ignore
import tsapp
import sys

window = tsapp.GraphicsWindow()
background = tsapp.Sprite("/app/background/WoodenRoomWithShelves.png", 0, 0)
window.add_object(background)

images = []
pizzas = []

uncooked_pizza_status = False
baked_pizza_status = False

oven, bowl, uncooked_pizza, baked_pizza = get_sprites(window, images, pizzas)

print("Welcome to Che's Pizza Parlor. It's Pizza Time!\n")

try:
    user_input = input("Would you like to bake a pizza with Che? | Answer (Y) or (N): ").strip().upper()
    if user_input == "Y":
        print("Great! Let's bake.")
    else:
        print("Goodbye!")
        sys.exit()
except (KeyboardInterrupt, EOFError):
    print("Invalid input, try again.")

print("\n\n\n\n")
print("Drag the ingredients on the shelves into the bowl to make a pizza.")
print("Make sure you don't drop one of the items because they get left behind!")

while window.is_running:
    mouse_x, mouse_y = tsapp.get_mouse_position()
    for image in images:
        if image.is_colliding_point(mouse_x, mouse_y) and tsapp.is_mouse_down():
            image.center_x, image.center_y = mouse_x, mouse_y

    if not uncooked_pizza_status and all(image.is_colliding_rect(bowl) for image in images):
        print("\n\n\n\nNice pizza! Let's bake it now.")
        print("Drag the uncooked pizza into the warm oven.")
        print("Don't burn yourself now, it's been 2 hours!")
        uncooked_pizza_status = True
        pizzas[0].visible = True        

    if not baked_pizza_status and uncooked_pizza_status and pizzas[0].is_colliding_rect(oven):
        print("\n\n\n\n")
        bake_timer()
        pizzas[0].visible = False
        pizzas[1].visible = True
        baked_pizza_status = True
        print("\n\n\n\nChe has his final Sayso: He loves your pizza! ENJOY YOUR LIFE and ENJOY THAT PIZZA.")

    if pizzas[0].visible and pizzas[0].is_colliding_point(mouse_x, mouse_y) and tsapp.is_mouse_down():
        pizzas[0].center_x, pizzas[0].center_y = mouse_x, mouse_y
        for image in images:
            image.visible = False

    elif not pizzas[0].visible and pizzas[1].visible and pizzas[1].is_colliding_point(mouse_x, mouse_y) and tsapp.is_mouse_down():
        pizzas[1].center_x, pizzas[1].center_y = mouse_x, mouse_y
    
    window.finish_frame()